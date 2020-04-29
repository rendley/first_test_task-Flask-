from wtforms import Form, StringField, validators, ValidationError
from app.models import Author


class AddAuthor(Form):
    first_name = StringField("Имя Автора", [validators.DataRequired()])

    def validate_first_name(self, first_name):
        author_count = Author.query.filter_by(first_name=first_name.data).count()
        if author_count > 0:
            raise ValidationError("Введенный вами автор уже существует")

        