from flask import flash, redirect, render_template, request, url_for
from app import db, app
from app.authors.forms import AddAuthor
from app.models import Author




@app.route("/author")
def author():
    # books = Book.query.order_by(Book.id.desk()).all() # поо дате дате добавления но нужно datetime в модель
    authors = Author.query.all()
    return render_template("book_and_author.html", authors=authors, title="Список Авторов")

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

@app.route("/updateauthor/<int:id>", methods=["POST", "GET"])
def update_author(id):
    print("hello")
    author = Author.query.get_or_404(id)   
    # book = Book.query.filter(Book.id==id).first()    
    if request.method == 'POST': 
        form = AddAuthor(formdata=request.form, obj=author)
        form.populate_obj(author)   
        db.session.commit()
        flash(f'Вы успешно изменили книгу', 'success')
        return redirect(url_for("author"))
    form = AddAuthor(obj=author)
    return render_template("edit_book_and_author.html", form=form, author=author)


@app.route("/deleteauthor/<int:id>", methods=["POST", "GET"])
def delete_author(id):
    author = Author.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(author)
        flash(f'Вы успешно удалили автора', 'success')
        db.session.commit()
        return redirect(url_for("author"))
    flash(f'Не удалось удалить автора', 'danger')
    return redirect(url_for("author"))