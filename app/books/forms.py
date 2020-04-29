from wtforms import Form, StringField, validators, ValidationError
from app.models import Book


class AddBook(Form):
    title = StringField("Название книги", [validators.DataRequired()])

    def validate_title(self, title):
        book_count = Book.query.filter_by(title=title.data).count()
        if book_count > 0:
            raise ValidationError("Введенный вами автор уже существует")