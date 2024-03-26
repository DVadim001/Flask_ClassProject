from flask import Blueprint, render_template
from user.forms import RegisterForm, LoginForm

user_bp = Blueprint('users', __name__, url_prefix='/user')


@user_bp.route('/')
def home_user():
    reg_url = '</br><a href="/user/register">Зарегистрироваться</a></br>'
    login_url = '</br><a href="/user/login">Логин</a></br>'
    return f'Привет. Выберите действие {reg_url+login_url}'


@user_bp.route('/register')
def register_user():
    # Назначение переменной для связки с формой
    form = RegisterForm()
    return render_template('register.html', form=form)


@user_bp.route('/login')
def login_user():
    # Назначение переменной для связки с формой
    login = LoginForm()
    return render_template('login.html', login=login)
