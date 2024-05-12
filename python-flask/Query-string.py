from flask import Flask
from flask import request
app=Flask(__name__,static_folder="public",static_url_path="/")  
#建立getsum的路徑
#利用query string要求字串提供彈性 /getsum?max= 
@app.route("/getsum")
def getsum():
    maxnumber=request.args.get("max",100)
    maxnumber=int(maxnumber)     #一定要轉int
    minnumber=request.args.get("min",1)
    minnumber=int(minnumber)
    result=0
    for n in range(minnumber,maxnumber+1):
        result+=n
    return "結果:"+str(result)

@app.route("/")
def index():       
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello Flask"
    else:
        return "歡迎光臨"

app.run(port=3000)  