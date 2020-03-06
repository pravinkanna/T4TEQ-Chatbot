from flask import Flask, escape, request, render_template, url_for
from Model import chatbotMain
from flask_socketio import SocketIO,send,emit

app = Flask(__name__)

app.config['SECRET_KEY'] = '43c018686f6f8dee825420285a01f0ba'

socketio = SocketIO(app)

@socketio.on('userQuery')
def handleConnection(json):
    query = str(json['data'])
    response = chatbotMain(query)
    print('query: ' + query)
    print('response:' + response)
    socketio.emit("backendResponse",response)

@app.route('/',methods=['GET'])
def chatbot():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app)