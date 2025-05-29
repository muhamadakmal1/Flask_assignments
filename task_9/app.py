from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((b for b in books if b['id'] == id), None)
    return jsonify(book) if book else ('Not Found', 404)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    updated_book = request.get_json()
    for book in books:
        if book['id'] == id:
            book.update(updated_book)
            return jsonify(book)
    return ('Not Found', 404)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [b for b in books if b['id'] != id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
