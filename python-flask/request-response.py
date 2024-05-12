from flask import Flask
from flask import request
from flask import redirect
import json
app=Flask(__name__,static_folder="public",static_url_path="/")  
@app.route("/en/")
def index_en():
    return json.dumps({
        "status": "ok",
        "text":"Hello Flask"
    })
@app.route("/zh/")
def index_zh():
    return json.dumps({
        "status":"ok",
        "text":"歡迎光臨"
    },ensure_ascii=False)  #不要用ascii編碼處理中文
@app.route("/")
def index():       
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")
    else:
        return redirect("/zh/")
        
app.run(port=3000)  