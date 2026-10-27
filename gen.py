#!/usr/bin/env python3
"""Generate or edit images with the Gemini image API.

The API key is attached by the environment's network proxy as an
x-goog-api-key header, so this script never reads or needs a key.

Usage:
  python3 gen.py models
      List models that can generate images.
  python3 gen.py run --out frames/S01 --n 4 --aspect 9:16 \
      --prompt-file prompts/S01.txt --ref cast/R-B.png --ref cast/R-F.png
      Writes frames/S01_a.png, S01_b.png ... (one API call per option).
      For "edit of Sxx" shots, pass the chosen earlier frame as the FIRST --ref.

Options:
  --model    image model id (default: $GEMINI_IMAGE_MODEL or gemini-2.5-flash-image)
  --prompt   prompt text inline, instead of --prompt-file
"""
import argparse, base64, json, mimetypes, os, string, sys, time, urllib.request, urllib.error

API = "https://generativelanguage.googleapis.com/v1beta"
DEFAULT_MODEL = os.environ.get("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image")


def call(url, body=None, timeout=180):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET",
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:800]}")


def list_models():
    res = call(f"{API}/models?pageSize=200")
    for m in res.get("models", []):
        name = m["name"].split("/")[-1]
        if "image" in name or "imagen" in name:
            print(name, "|", ", ".join(m.get("supportedGenerationMethods", [])))


def part_for(path):
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        return {"inline_data": {"mime_type": mime, "data": base64.b64encode(f.read()).decode()}}


def run(a):
    prompt = a.prompt or open(a.prompt_file).read()
    parts = [part_for(p) for p in a.ref] + [{"text": prompt}]
    body = {
        "contents": [{"parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE"],
                             "imageConfig": {"aspectRatio": a.aspect}},
    }
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    url = f"{API}/models/{a.model}:generateContent"
    for i in range(a.n):
        res = call(url, body)
        imgs = [p["inlineData"]["data"] for c in res.get("candidates", [])
                for p in c.get("content", {}).get("parts", []) if "inlineData" in p]
        if not imgs:
            print(f"option {i+1}: no image returned:", json.dumps(res)[:500])
            continue
        path = f"{a.out}_{string.ascii_lowercase[i]}.png"
        with open(path, "wb") as f:
            f.write(base64.b64decode(imgs[0]))
        print("wrote", path)
        time.sleep(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("models")
    r = sub.add_parser("run")
    r.add_argument("--out", required=True)
    r.add_argument("--n", type=int, default=4)
    r.add_argument("--aspect", default="9:16")
    r.add_argument("--prompt")
    r.add_argument("--prompt-file")
    r.add_argument("--ref", action="append", default=[])
    r.add_argument("--model", default=DEFAULT_MODEL)
    a = ap.parse_args()
    if a.cmd == "models":
        list_models()
    else:
        if not (a.prompt or a.prompt_file):
            sys.exit("give --prompt or --prompt-file")
        run(a)
