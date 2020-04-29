from wtforms import Form, StringField, validators


class AddAuthor(Form):
    first_name = StringField("Имя Автора", [validators.DataRequired()])