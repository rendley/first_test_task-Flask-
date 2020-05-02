from flask import flash, redirect, render_template, request, url_for, current_app
from app import db, app
from app.books.forms import AddBook
from app.models import Book, Author, User

from flask_login import login_required



@app.route("/home/")
def home():
    q = request.args.get("q")
    page = request.args.get("page")
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if q:
        books = Book.query.filter(Book.title.contains(q))
    else:
        books = Book.query
    pages = books.paginate(page=page, per_page=15)
    return render_template("home.html", books=books, pages=pages)


@app.route("/book")
@login_required
def book():
    books = Book.query.all()
    return render_template("view_book_and_author.html", books=books, title="Список книг")


@app.route("/createbook", methods=["POST", "GET"])
@login_required
def create_book():
    form = AddBook(request.form)
    if request.method == 'POST' and form.validate():
        book = Book(title=form.title.data)
        db.session.add(book)
        db.session.commit()
        flash(f'Вы успешно добавили книгу "{book.title}" в нашу библиотеку', 'success')
        return redirect(url_for('create_book'))  
    return render_template("create_book_and_author.html", form=form, book="book")


@app.route("/updatebook/<int:id>", methods=["POST", "GET"])
@login_required
def update_book(id):
    book = Book.query.get_or_404(id)      
    if request.method == 'POST': 
        form = AddBook(formdata=request.form, obj=book)
        form.populate_obj(book)   
        db.session.commit()
        flash(f'Вы успешно изменили книгу', 'success')
        return redirect(url_for("book"))
    form = AddBook(obj=book)
    return render_template("edit_book_and_author.html", form=form, book=book, books="books")


@app.route("/deletebook/<int:id>", methods=["POST", "GET"])
@login_required
def delete_book(id):
    book = Book.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(book)
        flash(f'Вы успешно удалили книгу', 'success')
        db.session.commit()
        return redirect(url_for("book"))
    flash(f'Не удалось удалить книгу', 'danger')
    return redirect(url_for("home"))




