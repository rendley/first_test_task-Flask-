from wtforms import Form, StringField, validators, ValidationError
from app.models import Book


class AddBook(Form):
    title = StringField("Name book", [validators.DataRequired()])

    def validate_title(self, title):
        book_count = Book.query.filter_by(title=title.data).count()
        if book_count > 0:
            raise ValidationError("Введенная вами книга уже существует!")