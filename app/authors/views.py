from flask import flash, redirect, render_template, request, url_for
from app import db, app
from app.authors.forms import AddAuthor
from app.models import Author



@app.route("/createauthor", methods=["POST", "GET"])
def create_author():
    form = AddAuthor(request.form)
    if request.method == 'POST' and form.validate():
        author = Author(first_name=form.first_name.data)
        db.session.add(author)
        db.session.commit()
        flash(f'Вы успешно добавили автора "{author.first_name}" в нашу библиотеку', 'success')
        return redirect(url_for('create_author'))  
    return render_template("create_book_and_author.html", form=form)