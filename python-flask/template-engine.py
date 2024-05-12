from flask import Flask
from flask import request
from flask import render_template
from flask import session
app=Flask(__name__,static_folder="public",static_url_path="/") 
app.secret_key="any string but secret"  #設定密鑰for session
@app.route("/") #使用get方法建立路徑/的函式
def index():
    return render_template("index3.html")   #template底下的資料夾!

@app.route("/show")
def show():
    name=request.args.get("name","")
    return "Hello "+name

@app.route("/hello") #/hello?name= 
def hello():
    name=request.args.get("name","")
    session["username"]=name  #session["column name"]=data 把name放入session裡面 連接hello&talk兩個關係
    return "Hello "+name
@app.route("/talk")
def talk():
    name=session["username"]
    return name+ " nice to meet you"

@app.route("/calculate", methods=["post"])
def cal():
    # 以下是接收get方法的query string
    # Number=request.args.get("max","")
    #接收post方法: 比較隱密安全 不會出現?
    Number=request.form["max"]
    Number=int(Number)
    result=0
    for n in range(Number+1):
        result+=n
    return render_template("result.html",data=result)  #參數data 在html用{{}}來帶出來動態資料

@app.route("/page")
def page():
    return render_template("page.html",name="Robinson")  #name帶入動態資料
app.run(port=3000)