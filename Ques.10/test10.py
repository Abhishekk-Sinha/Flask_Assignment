#10. Design a Flask app with proper error handling for 404 and 500 errors.


from flask import Flask, render_template, abort

app = Flask(__name__)

# Custom 404 error handler
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Custom 500 error handler
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# Example route that triggers a 404 error
@app.route('/not_found')
def trigger_not_found_error():
    # Imagine a situation where the resource is not found
    # You can raise a NotFound exception to trigger the 404 error handler
    abort(404)

# Example route that triggers a 500 error
@app.route('/internal_server_error')
def trigger_internal_server_error():
    # Imagine a situation where there's a server-side error
    # You can raise an Exception to trigger the 500 error handler
    raise Exception("Simulating an internal server error")

# Example route for a regular page
@app.route('/')
def home():
    return "Welcome to my Flask app!"

if __name__ == '__main__':
    app.run(debug=True)
