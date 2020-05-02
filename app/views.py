from flask import flash, redirect, render_template, request, url_for
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User


@app.route('/')
def index():
    return render_template('base.html', title="Библиотека")

@app.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)       
        db.session.commit()
        flash('Спасибо за регистрацию', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Регистрация", form=form)

@app.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)   
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Добро пожаловать на сайт', 'success')
            return redirect(url_for('home'))
        else:
            flash("Неправильная электронная почта или пароль", 'danger')   
            return redirect(url_for('login')) 
    return render_template('login.html', title="Авторизация", form=form)
