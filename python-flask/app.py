from flask import Flask
#建立application 物件
app=Flask(
    __name__,
    static_folder="public",           #靜態檔案對應的資料夾名稱 default=static
    static_url_path="/"               #靜態檔案對應的網址路徑 可以自行設定
)  
#建立路徑/
@app.route("/")
def index():    #用來回應路徑/的函式
    return "Hello Flask"

@app.route("/data")
def get_data():    
    return "MY data 10731"

#建立動態路由 <> 裡面參數是動態的
@app.route("/user/<name>")
def user_name(name):
    if name=="澎澎":
        return "你好 " + name
    else:
        return "Hello " + name
app.run(port=3000)   #啟動網站伺服器 可透過port=? 來指定port name

