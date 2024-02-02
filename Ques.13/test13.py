#Ques.13. Implement notifications in a Flask app using websockets to notify users of updates.

#import Flask and other necessary Module  for creating a Flask application and adding WebSocket support with Flask-SocketIO.
from flask import Flask, render_template
from flask_socketio import SocketIO

# create Flask application and socketIO instance
app = Flask(__name__)
socketio = SocketIO(app)

# Define the route forthe index page
@app.route('/')
def index():
    return render_template('index.html')

#Define SocketIO Event Handlers
@socketio.on('connect') # decorator indicates that the func. should be called when a webSocket connection is established, print 'connected'
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

#Run the flask application if the script in the main script & after that start the debuging process.
if __name__ == '__main__':
    socketio.run(app, debug=True)
