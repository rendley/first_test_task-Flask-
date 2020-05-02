from flask import flash, redirect, render_template, request, url_for
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User

from flask_login import login_user, logout_user, current_user
from app import login_manager

# check users LoginManager coockes user_id
# LoginManager check user_id in bd
@login_manager.user_loader 
def load_user(user_id): 
    return User.query.get(user_id)


@app.route('/')
def index():
    return redirect(url_for("home"))

@app.route('/register/', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
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
    if current_user.is_authenticated:
        return redirect(url_for("home"))      
    form = LoginForm(request.form)   
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Добро пожаловать на сайт', 'success')
            return redirect(url_for('home'))
        else:
            flash("Неправильная электронная почта или пароль", 'danger')   
            return redirect(url_for('login')) 
    return render_template('login.html', title="Авторизация", form=form)

@app.route("/logout/")
def logout():
    logout_user()
    flash("Вы успешно разлогинились", 'danger') 
    return redirect(url_for('home'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

