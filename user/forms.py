from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired


# Форма для регитсрации
class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired('Заполните это поле')])
    email = EmailField('Почта', validators=[DataRequired('Заполните это поле')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполните это поле')])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired('Заполните это поле')])
    button = SubmitField('Зарегистрироваться')


# Форма для логина
class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired('Заполните это поле')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполните это поле')])
    button = SubmitField('Войти')
