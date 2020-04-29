from flask import flash, redirect, render_template, request, url_for
from app import db, app
from app.books.forms import AddBook
from app.models import Book, Author



@app.route("/createbook", methods=["POST", "GET"])
def create_book():
    form = AddBook(request.form)
    if request.method == 'POST' and form.validate():
        book = Book(title=form.title.data)
        db.session.add(book)
        db.session.commit()
        flash(f'Вы успешно добавили книгу "{book.title}" в нашу библиотеку', 'success')
        return redirect(url_for('create_book'))  
    return render_template("create_book_and_author.html", form=form, book="book")


