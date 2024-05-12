from flask import Flask
from flask import request
app=Flask(__name__,static_folder="public",static_url_path="/")  

@app.route("/")
def index():    
    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址",request.url)
    # print("瀏覽器作業系統",request.headers.get("user-agent"))
    # print("語言偏好",request.headers.get("accept-language"))
    # print("引薦網址",request.headers.get("referrer"))
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello Flask"
    else:
        return "歡迎光臨"

app.run(port=3000)  