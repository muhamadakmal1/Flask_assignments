from flask_socketio import emit

from flask import Flask, render_template
from flask_socketio import SocketIO, send

from flask_socketio import emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

counter = 0

@socketio.on('increment')
def increment_counter():
    global counter
    counter += 1
    emit('update', counter, broadcast=True)


@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handleMessage(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

