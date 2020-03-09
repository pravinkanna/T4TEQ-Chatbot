from flask import Flask, escape, request, render_template, url_for
from Model import chatbotMain
import pymongo
import datetime
from database import insertIntoDB

app = Flask(__name__)

app.config['SECRET_KEY'] = '43c018686f6f8dee825420285a01f0ba'

myClient = pymongo.MongoClient("mongodb+srv://admin:pk123456@cluster0-rwpek.mongodb.net/test?retryWrites=true&w=majority")

myDb = myClient["Chatbot"] 

myCol = myDb["messages"]

@app.route('/', methods=['GET'])
def chatbot():
    return render_template('index.html')

@app.route("/get", methods=['GET'])
def get_bot_response():
    query = request.args.get('msg')
    response = chatbotMain(query)
    insertIntoDB(query,response)
    return str(response)

if __name__ == "__main__":
    app.run()