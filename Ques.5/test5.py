'''Ques.5. Implement user sessions in a Flask app to store and display user-specific data.'''

#Import necessary modules from Flask. Flask is the main Flask class, and other modules are used for rendering templates, handling requests, managing sessions, and redirects.
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session


app = Flask(__name__) #Create a Flask web application instance.

#Configure the Flask app for session management. 
# SESSION_PERMANENT is set to False to make the session temporary. 
# SESSION_TYPE is set to "filesystem," meaning session data will be stored on the server's file system.

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app) #Initialize the Flask-Session extension with the created Flask app

@app.route('/') #route for the root URL ("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html", name=session["name"])


#Define a route for the "/login" URL with support for both GET and POST methods. 
# If the method is POST (i.e., form submission), it stores the entered name in the session and redirects to the root URL. 
# If it's a GET request, it renders the "login.html" template.

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

#Define a route for the "/logout" URL. It sets the "name" in the session to None 
# and redirects to the login page.
@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")
    
#Run the Flask app if the script is executed directly. 
# The app will run on the specified host and port with debugging enabled.

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5009, debug = True)


