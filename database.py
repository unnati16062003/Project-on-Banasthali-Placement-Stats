import pandas as pd
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client['admin']
collection4=db["BanasthaliID"]
alldata=collection4.find()
yrs=[]
for item in alldata:
        print (type(item['StudentsYear']))
        if item['StudentsYear'] not in yrs:
              yrs.append(item["StudentsYear"])
print(yrs)             