import pymongo
import datetime

myClient = pymongo.MongoClient("mongodb+srv://admin:pk123456@cluster0-rwpek.mongodb.net/test?retryWrites=true&w=majority")

myDb = myClient["Chatbot"] 

myCol = myDb["messages"]

def insertIntoDB(query, response):
    myDict = {"Date":datetime.datetime.now().strftime("%x"),"Time":datetime.datetime.now().strftime("%X"), "query": query, "response": response }
    x = myCol.insert_one(myDict)

