#7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.

# Imports classes and functions from the Flask framework for building web applications.
from flask import Flask, render_template, request, redirect, url_for

# Import this class which provides SQL database support for Flask applications.
from flask_sqlalchemy import SQLAlchemy

# Create Flask web application instance & the __name__ argument is used to determine the root path of the application.
app = Flask(__name__)

# Set the URL for SQLite database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # Fix typo in 'URI'

# SQLAlchemy modification tracking, as it is not needed 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy database instance, connecting it to the Flask application.
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):

    # Define the column for the task id
    id = db.Column(db.Integer, primary_key=True)

    # Defines the column for the task content with a maximum length of 200 characters.
    content = db.Column(db.String(200), nullable=False)

@app.route('/')  # define a route for the root url & Decorate

# Function that queries all tasks from the database and renders the 'index.html' template with the list of tasks
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# Decorate that define the route for handling POST requests to add the tasks
@app.route('/add', methods=['POST'])

# Function that retrieves the task content from the form, adds a new task to the database, commits, and redirects to the home page
def add_task():
    content = request.form.get('content')
    if content:
        new_task = Task(content = content)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)


