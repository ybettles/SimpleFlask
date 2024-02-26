from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, NumberRange, EqualTo


class NumberForm(FlaskForm):
    numberField = IntegerField('Enter a number to check if it\'s prime:',
                               validators=[InputRequired(message="You can't submit an empty response!"),
                                           NumberRange(min=0, message="Please provide positive integer")])
    submitField = SubmitField("Check primality!")


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirmPassword = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Submit")
