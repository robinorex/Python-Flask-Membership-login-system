import pymongo
#connect to MongoDB
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

uri = "mongodb+srv://robinrucktheroom:root1234@cluster0.np1v1dh.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
print("connection sucess")
db=client.member_system #資料庫
from flask import *
app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key="any string but secret"
@app.route("/") #首頁
def main():
    return render_template("main.html")
@app.route("/member") #會員登入頁
def member():
    if "nickname" in session:  #權限控管
        return render_template("member.html")
    else:
        redirect("/")

@app.route("/error") #登入錯誤頁 要設定成/error?msg=
def error():
    message=request.args.get("msg","Error Happened please contact customer service") #就會變成?msg
    return render_template("error.html",message=message)
@app.route("/signup",methods=["POST"])
def signup():  #前端-->後端-->資料庫
    #從前端傳遞資料
    nickname=request.form["nickname"]
    email=request.form["email"]
    password=request.form["password"]
    #根據接收到的資料與資料庫互動
    collection=db.user
    result=collection.find_one({
        "email":email  #檢查email有沒有重複
    })
    if result != None:
        return redirect("/error?msg=email has been used")
    collection.insert_one({
        "nickname":nickname,
        "email":email,
        "password":password
    })
    return redirect("/")
@app.route("/signin",methods=["POST"])
def signin():
    #從前端取得使用者的輸入 
    email=request.form["email"]
    password=request.form["password"]
    collection=db.user
    result=collection.find_one({
        "$and":[{"email":email},{"password":password}]
    })
    if result==None:  #找不到資料 登入失敗
        return redirect("/error?msg=wrong email or password") 
    #登入成功 把result裡面的nickname放入 session中 紀錄會員資訊
    session["nickname"]=result["nickname"]
    return redirect("/member") 

@app.route("/signout")
def signout():
    del session["nickname"] #移除session中的會員資訊
    return redirect("/")
app.run(port=3000)