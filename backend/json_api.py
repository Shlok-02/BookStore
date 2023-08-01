# from flask import Flask,jsonify,request
# from http import HTTPStatus
# from book_store import books
#
# app = Flask(__name__)#creates Flask class instance
# if __name__ == '__main__': #starts the flask server
#      app.run(use_reloader=True)
#
# @app.route('/',methods=['GET'])
# def get_books():
#      return jsonify({"books_data":books})
#
# @app.route('/create',methods=['POST'])
# def create_book():
#
#      data = request.get_json()
#      for book in books:
#           if book['book_title']==data['book_title']:
#                return jsonify({"Error": "Book already present"})
#
#
#      title=data['book_title']
#      author=data['book_author']
#      publisher=data['publisher']
#      description=data['description']
#      id=len(books)+1
#      newBook={
#           "id":id,
#           "book_title":title,
#           "book_author":author,
#           "publisher":publisher,
#           "description":description
#      }
#
#      books.append(newBook)
#
#      return jsonify({"status code":201})
#
# @app.route('/update',methods=['PUT'])
# def update_book():
#      data=request.get_json()
#
#      for book in books:
#           if book['book_title']==data['book_title']:
#                book.update(
#                     {
#                          'book_title': data.get('book_title'), 'book_author': data.get('book_author'),
#                          'publisher': data.get('publisher'), 'description': data.get('description'),
#                     }
#                )
#                return jsonify(book)
#
#
# @app.route('/delete/<int:book_id>',methods=['DELETE'])
# def delete_book(book_id):
#
#      for i in range(0,len(books)):
#           if books[i].get('id')==book_id:
#                del books[i]
#      return jsonify(books)
#
# @app.route('/book/<int:book_id>',methods=['GET'])
# def get_book(book_id):
#
#      for i in range(0,len(books)):
#           if books[i].get('id')==book_id:
#                return jsonify(books[i])
#
#      return jsonify({"Error":"book not found"})