from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up SQLite database (books.db will be created)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Book model (table in the database)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)

# Route to display the form to add a book
@app.route('/')
def home():
    return render_template('index.html')

# Route to add a new book
@app.route('/add_book', methods=['POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        
        new_book = Book(title=title, author=author, genre=genre)
        
        try:
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('books'))  # Redirect to the list of books after adding
        except:
            return 'There was an issue adding your book'

# Route to display all books
@app.route('/books')
def books():
    all_books = Book.query.all()
    return render_template('books.html', books=all_books)

# Create tables and run the Flask app when the script is executed directly
if __name__ == '__main__':
    with app.app_context():  # Ensure the app context is set before creating tables
        db.create_all()  # Manually create all tables
    app.run(debug=True, host='0.0.0.0', port=5000)

