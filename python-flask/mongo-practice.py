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
#把資料放進資料庫db中
# db=client.test   #選擇操作test資料庫
# collection=db.users #選擇操作users集合
# #新增資料到雲端
# collection.insert_one({
#     "name":"Robin",
#     "gender":"male"
# })
db=client.mywebsite #資料庫
collection=db.users #集合
# result=collection.insert_many([{
#     "name": "JOhnson",
#     "email":"johnbo@gmail.com",
#     "password":"test",
#     "level": 2
# },{
#     "name": "Bobo",
#     "email":"bpbo@gmail.com",
#     "password":"test",
#     "level": 3
# }])
# result=collection.insert_one({ #文件
#     "name": "Robin",
#     "email":"robinrucktheroom@gmail.com",
#     "password":"test",
#     "level": 1
# })
# print("Data insert success")
# print(result.inserted_id)
#取得集合中的第一筆資料
# data=collection.find_one()
# print(data)
# data=collection.find_one(
#     ObjectId("663b1bae4146ce09c95c64ec")
# )
# print(data)
# #取得特定欄位
# print(data["_id"])
# print(data["email"])
#一次取得多筆文件資料
# cursor=collection.find()
# # print(cursor)
# for doc in cursor:
#     print(doc["name"])
#update the data in collection:
# result=collection.update_one({
#     "email":"robinrucktheroom@gmail.com"   #篩選條件
# },{
#     "$set":{"password":"ply"}   #要覆蓋的資料
# })
# print("符合條件的文件數量",result.matched_count)
# print("實際更新的文件數量",result.modified_count)
# result=collection.update_one({
#     "email":"robinrucktheroom@gmail.com"   #篩選條件
# },{
#     "$unset":{"password":"ply"}   #unset直接刪除password這個欄位
# })
# result=collection.update_one({
#     "email":"robinrucktheroom@gmail.com"   #篩選條件
# },{
#     "$inc":{"level":5}   #increase level 增加5
# })
# result=collection.update_one({
#     "email":"robinrucktheroom@gmail.com"   #篩選條件
# },{
#     "$mul":{"level":2}   #multiple level *2
# })
# print("符合條件的文件數量",result.matched_count)
# print("實際更新的文件數量",result.modified_count)
# result=collection.update_many({
#     "level":3
# },{"$set":{"level":5}})
# print("符合條件的文件數量",result.matched_count)
# print("實際更新的文件數量",result.modified_count)
# result=collection.delete_one({
#     "email":"johnbo@gmail.com"
# })
# result=collection.delete_many({
#     "level":5
# })
# print(result.deleted_count)
# doc=collection.find_one({
#     "email":"robinrucktheroom@gmail.com"
# })
# print(doc["name"])
#複合篩選條件
# doc=collection.find_one({
#     "$and":[{
#     "email":"robinrucktheroom@gmail.com"},
#     {"password":"test"
#     }]
# }) #$and兩個條件都要滿足
cursor=collection.find({
    "$or":[{
        "email":"robinrucktheroom@gmail.com"
    },{
        "level":2
    }]
},sort=[("level",pymongo.DESCENDING)])#$or任意滿足即可  排序
for doc in cursor:
    print(doc)