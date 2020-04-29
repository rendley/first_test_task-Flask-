from wtforms import Form, StringField, validators


class AddBook(Form):
    title = StringField("Название книги", [validators.DataRequired()])