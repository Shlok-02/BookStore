from cs50 import SQL
from flask import Flask, jsonify, request
from http import HTTPStatus
from book_store import books


# to initialize connection to DB
db = SQL("sqlite:///database.db")

# create a tables for books named Books


## create a table
# db.execute(("create table if not exists books (id INTEGER PRIMARY KEY AUTOINCREMENT,book_title string,book_author string,publisher string,description string)"))

## to insert some data in Table
# db.execute("INSERT INTO books(book_title,book_author,publisher,description) VALUES(?,?,?,?)" , "GOD of WAR","Jack Hughman","chowa","war history")
# db.execute("INSERT INTO books(book_title,book_author,publisher,description) VALUES(?,?,?,?)" , "Splinter cell","Tom clancy","cross","splinting of cells")
# db.execute("INSERT INTO books(book_title,book_author,publisher,description) VALUES(?,?,?,?)" , "Monsters","jackie bu","meme","are monster real")


app = Flask(__name__)  # creates Flask class instance
if __name__ == '__main__':  # starts the flask server
     app.run(use_reloader=True)


@app.route('/get', methods=['GET'])
def get_books():
     dbdata=db.execute("SELECT * from books")
     return jsonify({"books_data": dbdata})

@app.route("/create",methods=['POST'])
def create_book():

     data=request.get_json()
     dbdata=db.execute("SELECT * from books")

     print(dbdata)
     for book in dbdata:
           if book['book_title']==data['book_title']:
                return jsonify({"Error": "Book already present"})

     title = data['book_title']
     author=data['book_author']
     publisher=data['publisher']
     description=data['description']
     db.execute("INSERT INTO books(book_title,book_author,publisher,description) VALUES(?,?,?,?)" , title,author,publisher,description)

     return jsonify({"Success":"Book Added"})


@app.route('/update',methods=['PUT'])
def update_book():
     data=request.get_json()

     title = data['book_title']
     author=data['book_author']
     publisher=data['publisher']
     description=data['description']

     book_id=data['id']
     for book in books:
          if book['id']==book_id:
               db.execute("UPDATE books SET book_title= ? , book_author= ? , publisher=?,description =? WHERE ID = ?",title,author,publisher,description,book_id)
               return jsonify({"Success":"Book Updated Successfully"})

     return jsonify({"Error":"Book not present"})

@app.route('/delete/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
     #data = request.get_json()
     dbdata = db.execute("SELECT * from books")

     print(dbdata)
     for book in dbdata:
          if book['id'] == book_id:
               db.execute("DELETE FROM books where id= ?",book_id)
               return jsonify({"Success":"Book deleted Successfully"})

     return jsonify({"Error":"Book Not Present"})
