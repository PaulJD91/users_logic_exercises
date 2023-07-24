from flask import render_template,Blueprint,request,redirect
from models.book_list import book_list, Book

book_blueprint = Blueprint("book_list", __name__)

@book_blueprint.route('/')
def index():
    return render_template("index.jinja", title = "Library Home", book_list=book_list)

@book_blueprint.route('/books')
def list_of_books():
    return render_template("books.jinja", title = "List of Books", book_list=book_list)

