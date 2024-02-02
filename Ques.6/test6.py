# 6. Build a Flask app that allows users to upload files and display them on the website.

# Imports the os module, which provides a way to interact with the operating system, including file and directory operations.
import os

#Imports necessary classes and functions from the Flask framework, which is used to create web applications.
from flask import Flask, render_template, request, redirect, url_for

#function from Werkzeug, a utility library for WSGI applications. This function is used to sanitize filenames and prevent security issues.
from werkzeug.utils import secure_filename

# Creates a Flask web application instance. The __name__ argument is used to determine the root path of the application.
app = Flask(__name__)

#  Sets the upload folder where the uploaded files will be stored.
app.config['UPLOAD_FOLDER'] = 'uploads'

#: Defines the allowed file extensions for uploaded files.
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'gif'}

#A function that checks if the provided filename has an allowed extension. It returns True if the extension is allowed and False otherwise.
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Decorator that defines a route for the root URL.
@app.route('/')

# Function that renders the 'index.html' template when the root URL is accessed.
def index():
    return render_template('index.html')

# Decorator that defines a route for handling file uploads via POST requests.
@app.route('/upload', methods=['POST'])
def upload_file():  #Function that handles the file upload process.
    file = request.files.get('file')  #REtrived the upload file from the request.

    if not file or file.filename == '':   #Checks condition if a file is present and has a filename; if not, redirects to the previous URL.
        return redirect(request.url)

# Checks if the file has an allowed extension. If yes, it sanitizes the filename, creates the 'uploads' directory if it doesn't exist, and saves the file. Then, it redirects to the home page.
    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))

#If the file is not allowed, it redirects to the previous URL.
    return redirect(request.url)

# Decorator that defines a route for displaying uploaded files.
@app.route('/uploads/<filename>')

#Function that renders the 'uploaded.html' template with the provided filename if the file exists; otherwise, it returns a message indicating that the file is not found.
def uploaded_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if os.path.exists(file_path):
        return render_template('uploaded.html', filename=filename)
    else:
        return "File not found."

        # Checks if the script is being run directly .
if __name__ == '__main__':

    #Runs the Flask application on the specified host and port with debugging enabled. The host '0.0.0.0' makes the app accessible from the network.
    app.run(host='0.0.0.0', port=5009, debug=True)
