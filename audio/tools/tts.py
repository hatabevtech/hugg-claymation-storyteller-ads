import json,base64,urllib.request,urllib.error,wave,sys
STYLE="You are a warm, trustworthy Indian male narrator from Mumbai, speaking natural everyday Hindi (Hinglish) with a native Indian accent, like a friend explaining something important. Calm, clear, unhurried, with natural Hindi intonation and dental consonants. Read this:\n"
def tts(text, out, voice="Charon", model="gemini-3.8-flash-tts", lang="hi-IN", style=STYLE):
    sc={"voiceConfig":{"prebuiltVoiceConfig":{"voiceName":voice}}}
    if lang: sc["languageCode"]=lang
    body={"contents":[{"parts":[{"text":style+text}]}],"generationConfig":{"responseModalities":["AUDIO"],"speechConfig":sc}}
    req=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
    try: r=json.loads(urllib.request.urlopen(req,timeout=300).read())
    except urllib.error.HTTPError as e: print(out,"HTTP",e.code,e.read().decode()[:300]); return None
    pcm=base64.b64decode(r["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
    w=wave.open(out,"wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000); w.writeframes(pcm); w.close()
    return r.get("usageMetadata",{}).get("candidatesTokenCount")
if __name__=="__main__":
    print(tts(sys.argv[1],sys.argv[2],*sys.argv[3:]))
