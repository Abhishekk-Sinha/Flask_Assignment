# Q.11. Create a real-time chat application using Flask-SocketIO

#import the flask from'Flask module, which is used to create the Flask application'
# and import some important module, using FlaskSocketio module which is used to add Web Socket support to Flask appl. 

from flask import Flask, render_template
from flask_socketio import SocketIO, send

#create Flask app instance named app using Flask class
#__name__ is a special variable in python that represnts the name of the current module
app = Flask(__name__)
socketio = SocketIO(app) #it is conatructor, by passing the flask application

@app.route('/') #func. return the result of rendering the index.html
def index():
    return render_template('index.html')

@socketio.on('message') # when client sends the message, FlaskSocketIO will call the 'handle message'
def handle_message(message): # it represent the message sent by client
    print('Received message:', message)
    send('message', broadcast = True) #broadcast = true parameter indicate that the message shold be broadcasted to all client.

#This function will be called whenever a client connects to the server. It prints a message to the server console indicating that a client has connected.
@socketio.on('connect')
def handle_connect():
    print('Client connected')

# disconnect from the server & print msg disconnect if client disconnect
@socketio.on('disconnect')
def handle_disconnect():
    print('Client dissconnect')

#Run the flask application if the script in the main script & after that start the debuging process.
if __name__ == '__main__':
    socketio.run(app, host = "0.0.0.0", port=5009, debug=True)