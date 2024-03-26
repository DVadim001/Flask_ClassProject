from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


# Форма длярегитсрации
class CommentForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired('Заполните это поле')])
    title = StringField('Тема', validators=[DataRequired('Заполните это поле')])
    comment = TextAreaField('Коммент', validators=[DataRequired('Заполните это поле')])
    button = SubmitField('Зарегистрироваться')
