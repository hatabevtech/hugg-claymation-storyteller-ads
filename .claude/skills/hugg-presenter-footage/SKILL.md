---
name: hugg-presenter-footage
description: Turn a hugg ad script plus a character reference image into the full set of presenter keyframes (images only), one per presenter shot, in hugg's fixed set, each with a ready-to-paste Google Flow prompt (camera move, action, and the spoken line for lip-sync) so the user can generate the presenter footage in Flow. Use whenever the user gives a character and a script and wants presenter frames, talking-head shots, AI presenter footage, or "frames for Flow", even if they don't name this skill.
---

# hugg presenter footage: script + character → keyframes for Google Flow

The user gives you **a character (reference image or images)** and **a final script**. You produce every **presenter** shot as a still keyframe in hugg's fixed set, and hand them off with a Google Flow prompt per shot. The user animates them in Flow; that becomes the ad's presenter footage. Cutaways (B-roll, anatomy, graphics) are **not** generated. They appear in the shot list as placeholders.

The shot grammar below comes from studying YOGABODY presenter ads (`references/shot-grammar.md`). Use it for its *grammar* only. Never copy their presenter, set, wardrobe or branding.

## Inputs, and what to ask

- **Character reference image(s): required.** They are the locked look. Never regenerate or "improve" the character. Every frame is built from these images.
- **Wardrobe:** smart casual in a warm neutral (a plain shirt; no coat, no tie), unless the user says otherwise. If the reference image shows doctor clothing (white coat, stethoscope), keep the face, glasses and hair exactly and **replace the clothes**. The presenter is a host, not a doctor endorsing the product. Keep the same outfit for the whole ad.
- **Confirm the character is AI-generated,** or that a real person has given explicit consent to AI footage of themselves in hugg ads. Ask if it isn't clear. No image prompts until it's settled.
- **Script: required.** This is the final VO. Don't change a word. If a line looks wrong, raise it.
- **The hugg set**: `references/hugg-set.md` describes it. Once the user approves a set plate, it lives at `presenter/set/SET.png`. If that file doesn't exist yet, make the set plate first (Step 2) and get it approved. It is then reused for **every** ad.

Ask only for what's missing. Don't ask about stats or claims; this skill doesn't touch the words.

## Manual mode (no API key yet)
If the image API isn't available, run the same steps, but for each image step give the user:
- the ready-to-paste prompt;
- the images to attach, in order;
- the aspect ratio;
- how many options to make;
- the file names to send back (e.g. `P05_a`, `P05_b`).

Save the prompts to `prompts/` as usual. When the images come back, save them under `frames/`, run Step 4's checks on every one, and pick, or ask for specific re-rolls. Never make mock images yourself.

## Step 0: Check the image API
Run `python3 gen.py models` from the repo root. If it fails (e.g. 401 "API key not valid"), stop and tell the user to update the Gemini key in the environment's settings (Network secrets) and start a new session. Never ask for the key in chat, and never make mock frames. The shot list and the prompts (Steps 1 and 4's text) can still be written meanwhile.

## Step 1: Shot list (show it, get approval)
Split the script into shots of about **1.5–3 s each (roughly 4–8 spoken words)**, cutting at natural phrase breaks. Tag each shot:
- **P (presenter):** the hook, direct address to the viewer, the turn, counting ("number one…"), opinions, reactions, the product line, the CTA.
- **C (cutaway):** symptom lists that want visuals, mechanisms, stats, testimonials, product macro shots. Write one line on what the cutaway should show, then move on.

Aim for **presenter ≈ 50–60% of runtime**. Never put more than 3 C shots in a row without a P shot coming back.

For every P shot, decide: **size · gesture · expression · gaze · prop or demo**, using `references/shot-grammar.md`. Show the user a table:

| # | Time | Line | P/C | Size | Gesture | Expression | Notes |

and wait for approval before generating.

## Step 2: Set plate and anchor (show both, get approval)
1. **Set plate** (first time only): generate the empty hugg set from `references/hugg-set.md`, at 9:16, with nobody in it. After approval, save it as `presenter/set/SET.png` and commit it. It is reused for every ad from then on.
2. **Anchor for this ad**: the character, seated in the set, in a **wide** shot, neutral and calm, looking at the lens. Use `--ref presenter/set/SET.png --ref <character images>`. Generate 4 options, pick the one where the face matches the reference best, and get approval. Save it as `presenter/<ad>/final/P00.png`.

## Step 3: Generate the presenter shots as edits of the anchor
Every P shot is an **edit of the anchor**: pass `final/P00.png` as the **first** `--ref`, then the character image(s). Never generate a P shot from scratch. That is what keeps the face, outfit, set and light identical. Write each prompt to `presenter/<ad>/prompts/Pxx.txt` first, so every frame is reproducible.

Prompt pattern:
```
Edit this image. Same person, same face, same skin tone, same hair, same outfit, same set, same lighting as the image; the second image is the person's reference: match the face exactly.
Reframe as a [SIZE: wide full body seated / medium waist-up / close-up chest-up leaning slightly toward the lens / extreme close-up face].
[GESTURE in concrete terms, e.g. "right hand raised showing exactly three fingers, palm toward camera"].
Expression: [e.g. concerned, brows pulled together, mouth mid-word].
Looking straight into the lens. [PROP if any.]
Vertical 9:16; keep the person inside the central 4:5 area. Photorealistic, natural skin texture, soft high-key daylight, shallow depth of field. No text, no captions, no logos, no watermark.
```
Command:
```bash
python3 gen.py run --out presenter/<ad>/frames/P05 --n 2 --aspect 9:16 \
  --prompt-file presenter/<ad>/prompts/P05.txt \
  --ref presenter/<ad>/final/P00.png --ref <character image>
```
Use 2 options per shot (4 for the hook and the CTA). Work in **batches of about 6 shots**, in script order, and stop after each batch for the user's picks.

## Step 4: Check every option yourself
Open every PNG. Reject and re-roll anything that fails; don't present it.
- **Same person:** the face matches the reference, with the same skin tone (edits drift lighter; watch it), hair and age.
- **Same outfit, set and light** as the anchor. No new props or furniture.
- **Hands:** the right number of fingers, and counting gestures show the right count.
- **The gesture and expression match the line.**
- **The framing fits:** the person sits inside the central 4:5 area, and the middle third stays calm for captions.
- **No text anywhere:** no letters, logos or garbled writing.
- **Host, not doctor:** no white coat or stethoscope, no clinic.

Recommend one option per shot, with a one-line reason.

## Step 5: Hand off to Flow
After approval, copy the picks to `presenter/<ad>/final/Pxx.png` and write `presenter/<ad>/flow.md`: one block per P shot, in order.
```
### P05 · 0:07–0:09 · close-up
Frame: final/P05.png
Line: "Pet mein jaise patthar."
Flow prompt: Slow push-in. She leans slightly toward the camera, right hand pressed flat on her upper stomach, brows pulled together, and says in Hinglish with a warm, concerned tone: "Pet mein jaise patthar." Natural lip movement, subtle head motion, steady eye contact. No subtitles, no on-screen text, no music.
```
Rules for Flow prompts:
- One camera move per shot: slow push-in, static, or a gentle drift.
- The line goes in quotes, exactly as scripted, with "in Hinglish", plus one voice direction (warm, concerned, upbeat, emphatic).
- Clips are 8 s at most. If a P shot's line runs longer, split it into two shots.
- Add "No subtitles, no on-screen text" every time; captions are added in the edit.

Also list the C placeholders in `flow.md` (time, line, what to show), so the editor knows the gaps. Commit `prompts/`, `final/` and `flow.md` with a short message per batch.

## Format note
Google Flow outputs 9:16 or 16:9, and hugg's feed ads run at 4:5. Generate at **9:16** and keep the person and their gestures inside the **central 4:5 area**, so the edit can crop to 4:5 without cutting off hands or the head.
