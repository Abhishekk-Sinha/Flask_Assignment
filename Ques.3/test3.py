''' 3. Develop a Flask app that uses URL parameters to display dynamic content.'''
#import Flask and Necessary Modules
from flask import Flask, render_template

# Create Flask Application
app = Flask(__name__)

# Define Routes and View Functions
# this code define the root url'/' and associate it with the 'show_form' function.
#when a user access the url, the function renders the 'index.html' templates.
@app.route('/')
def show_form():
    return render_template("index.html")

#define the route for /today_news url with the post meethod.
# it retrives the value 'data' from the input data & print them. 

@app.route("/today_news", methods = ['POST'] )
def todays_news():
    #'args' is unusual for a POST requests, from the data is accessed.
    data = request.args.get('today_news')  #take any kind of input called request
    return f"{data}"  # func. return a response containg the value of 'today_news' parameter.

#Run the flask application if the script in the main script & after that start the debuging process.
if __name__== "__main__":
    app.run(host = "0.0.0.0", port=5004)