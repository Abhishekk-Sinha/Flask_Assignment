"""Ques. 2. Build a Flask app with static HTML pages and navigate between them.
"""

# Flask is a lib which help you out to perform the lib. which you help you to out to expose the output to expose your function in API.
from flask import Flask, render_template, request

#this will help you out to rapped this function(i will try to convert this entire application into the flask application )
app = Flask(__name__)

#Define the route & view functions
# This line uses a decorator (@app.route('/')) to associate the following function with the root URL ('/'). In Flask, routes are used to define the URLs that your application can handle.
@app.route('/')
def show_form():
    return render_template("index.html")

# define route for the check pass. URL with the POST method. It retrives the values of username & password
# from the data & print them. After that function simple response "..."
@app.route("/check_password", methods=['POST'])
def check_password():
    name = request.form.get('username')
    password = request.form.get('password')
    print({name}, {password})
    return "Username and password received"


# Run the flask application if the script in the main script & after that start the debuging process.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
