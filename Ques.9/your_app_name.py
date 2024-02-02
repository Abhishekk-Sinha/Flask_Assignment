#9. Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.

from flask import Flask, jsonify, request, render_template
#Import necessary modules from Flask, including Flask for creating the application instance, jsonify for JSON response formatting, request for handling HTTP requests, and render_template for rendering HTML templates.

app = Flask(__name__) #Create a Flask application instance

# Sample data for books
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

# Routes for CRUD operations on books
@app.route('/books', methods=['GET']) #Define a route for handling HTTP GET requests to the /books endpoint.
def get_books(): #andle the GET request. It returns a JSON response containing the list of books.
    return jsonify({"books": books})

#route for handling HTTP GET requests to the /books/<int:book_id> endpoint, where <int:book_id> is a variable representing the book's ID.
@app.route('/books/<int:book_id>', methods=['GET'])

# to handle the GET request. It retrieves a specific book by ID from the books list and returns a JSON response. If the book is not found, it returns a 404 error.
def get_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        return jsonify({"book": book})
    else: 
        return jsonify({"message": "Book not found"}), 404

# route for handling HTTP POST requests
@app.route('/books', methods=['POST'])

# to handle the POST request. It extracts JSON data from the request, creates a new book with an incremented ID, adds it to the books list, and returns a JSON response with a success message and the newly added book.
def add_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_book)
    return jsonify({"message": "Book added successfully", "book": new_book}), 201


# oute for handling HTTP PUT requests 
@app.route('/books/<int:book_id>', methods=['PUT'])

#o handle the PUT request. It retrieves a specific book by ID, updates its title and author with the data from the request, and returns a JSON response. If the book is not found, it returns a 404 error.
def update_book(book_id):
    data = request.get_json()
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        book["title"] = data["title"]
        book["author"] = data["author"]
        return jsonify({"message": "Book updated successfully", "book": book})
    return jsonify({"message": "Book not found"}), 404

#handling HTTP DELETE requests to the /books/<int:book_id> endpoint.
@app.route('/books/<int:book_id>', methods=['DELETE'])

# handle the DELETE request. It removes a specific book by ID from the books list and returns a JSON response with a success message.
def delete_book(book_id):
    global books
    books = [item for item in books if item["id"] != book_id]
    return jsonify({"message": "Book deleted successfully"}), 200



@app.route('/') # Define a route for handling HTTP GET requests to the root URL.
def index(): #Define a function index to render an HTML template
    return render_template('index.html')


if __name__ == '__main__': #Check if the script is being run directly
    app.run(host = "0.0.0.0", port = 5009, debug=True) #Run the Flask application in debug mode if the script is executed directly. This starts the development server.



