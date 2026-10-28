import json,base64,urllib.request,urllib.error,sys,mimetypes
def ask(path, question, model="gemini-3.8-flash"):
    mime={"wav":"audio/wav","mp3":"audio/mpeg","bin":"audio/mpeg","m4a":"audio/mp4"}[path.rsplit('.',1)[1]]
    body={"contents":[{"parts":[{"inline_data":{"mime_type":mime,"data":base64.b64encode(open(path,'rb').read()).decode()}},{"text":question}]}]}
    req=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
    try: r=json.loads(urllib.request.urlopen(req,timeout=300).read())
    except urllib.error.HTTPError as e: return f"HTTP {e.code} {e.read().decode()[:400]}"
    return "".join(p.get("text","") for p in r["candidates"][0]["content"]["parts"])
if __name__=="__main__": print(ask(sys.argv[1], sys.argv[2]))
