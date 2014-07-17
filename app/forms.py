from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(Form):
    username = TextField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])


class RegisterForm(Form):
    name = TextField('name', validators = [DataRequired()])
    username = TextField('username', validators = [DataRequired()])
    password = PasswordField('password',
        validators = [DataRequired(), EqualTo('confirmation', message = 'Passwords must match')])
    confirmation = PasswordField('confirmation', validators = [DataRequired()])


class TodoForm(Form):
    body = TextField('body', validators = [DataRequired()])