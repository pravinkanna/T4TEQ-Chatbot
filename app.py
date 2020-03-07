from flask import Flask, escape, request, render_template, url_for
from Model import chatbotMain

app = Flask(__name__)

app.config['SECRET_KEY'] = '43c018686f6f8dee825420285a01f0ba'

@app.route('/',methods=['GET'])
def chatbot():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
    response = chatbotMain(query)
    print("Query: ", query)
    print("Response: ", response)
    return str(response)

if __name__ == "__main__":
    app.run()