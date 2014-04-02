from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectMultipleField
from wtforms.validators import Required, ValidationError
from app.models import Author, User


class SignInForm(Form):
    username = TextField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])


class SignUpForm(Form):
    def uniqueUsername(self, field):
        if User.query.filter_by(username=field.data).all():
            raise ValidationError('This username is already taken')
    username = TextField('username', validators=[Required(), uniqueUsername])
    email = TextField('email', validators=[Required()])
    password = PasswordField('password', validators=[Required()])


class NewBookForm(Form):
    name = TextField('name', validators=[Required()])
    authors = SelectMultipleField(choices=[], coerce=int)


class NewAuthorForm(Form):
    def uniqueAuthor(self, field):
        if Author.query.filter_by(name=field.data).all():
            raise ValidationError('Author name must be unique')

    name = TextField('name', validators=[Required(), uniqueAuthor])