from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    emit('message', msg, broadcast=True)

@socketio.on('new_event')
def notify():
    emit('notification', "🔔 A new update just occurred!", broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)
