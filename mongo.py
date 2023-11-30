import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mongodbVSCodePlaygroundDB"]
mycol = mydb["sales"]

# mycol.insert_one({
#     "item": "canvas",
#     "quantity": 100,
#     "price": "$6.99"    
# })

x = mycol.find()

for i in x:
    print(i)


