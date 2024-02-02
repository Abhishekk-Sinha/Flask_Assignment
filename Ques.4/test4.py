'''4. Create a Flask app with a form that accepts user input and displays it.'''

# Import Flask aand some necessary Modules
from flask import Flask, render_template, request

# Create Flask  Application
web_app = Flask(__name__)

#Define the route & View function
@web_app.route('/', methods=['GET', 'POST']) 


# if the req method is POST i.e form submitted  & the route is associated with index function.
# & it retrives the user from the form & renders the 'index.html' temp. the user input.
# if the req method is GET, it renders the index.html template with 'user_input' set 'none'
def index():
    if request.method == 'POST':  
        user_input = request.form['user_input']
        return render_template('index.html', user_input=user_input)
    return render_template('index.html', user_input=None)

#
# Run the flask application if the script in the main script & after that start the debuging process.
if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5004, debug=True)