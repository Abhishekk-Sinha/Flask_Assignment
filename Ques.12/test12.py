#12. Build a Flask app that updates data in real-time using WebSocket connections.

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# initialize global variable 'counter' to keep connected client.
counter = 0

# route the index page
@app.route('/')
def index():
    return render_template('index.html', counter=counter)

#Socketio event handlers
@socketio.on('connect') 
def handle_connect():
    global counter
    counter += 1
    print('Client connected')
    socketio.emit('update_counter', {'counter': counter}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    global counter
    counter -= 1
    print('Client disconnected')
    socketio.emit('update_counter', {'counter': counter}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
