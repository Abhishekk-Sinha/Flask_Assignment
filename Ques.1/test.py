''' Ques. Create a Flask app that displays "Hello, World!" on the homepage.'''

from flask import Flask, request
# flask is a lib which is help you out to perform the libarary. which you help you out to expose your function in API

app = Flask(__name__)
#this will help you out to rapped this function(i will try to convert this entire application into the flask application )

@app.route('/') 
# This line uses a decorator (@app.route('/')) to associate the following function with the root URL ('/'). In Flask, routes are used to define the URLs that your application can handle.

def print_name():  #this is the function
    return f"Hello World !"

# Run the Flask application if this script is the main script
if __name__=='__main__':

    # This line starts the Flask development server with debugging enabled. 
    app.run(host = "0.0.0.0", port = 5004)
