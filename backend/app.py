from cs50 import SQL
from flask import Flask, jsonify, request
from http import HTTPStatus
from book_store import books


# to initialize connection to DB
db = SQL("sqlite:///database.db")

# create a tables for books named Books

# db.execute(("create table if not exists books (id INTEGER PRIMARY KEY AUTOINCREMENT,book_title string,book_author string,publisher string,description string)"))

# db.execute("INSERT INTO books(book_title,book_author,publisher,description) VALUES(?,?,?,?)" , "GOD of WAR","Jack Hughman","chowa","war history")
# db.execute("INSERT INTO books(book_title,book_author,publisher,description) VALUES(?,?,?,?)" , "Splinter cell","Tom clancy","cross","splinting of cells")
# db.execute("INSERT INTO books(book_title,book_author,publisher,description) VALUES(?,?,?,?)" , "Monsters","jackie bu","meme","are monster real")


app = Flask(__name__)  # creates Flask class instance
if __name__ == '__main__':  # starts the flask server
     app.run(use_reloader=True)


@app.route('/get', methods=['GET'])
def get_books():
     return jsonify({"books_data": books})