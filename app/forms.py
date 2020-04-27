from wtforms import Form, StringField, PasswordField, validators



class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=3, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


class LoginForm(Form):
    email = StringField('Email Address', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
