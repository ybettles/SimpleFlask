from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, NumberRange, EqualTo


class NumberForm(FlaskForm):
    numberField = IntegerField('Enter a number to check if it\'s prime:', validators=[InputRequired(message="You can't submit an empty response!"), NumberRange(min=0, message="Please provide positive integer")])
    submitField = SubmitField("Check primality!")

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirmPassword = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Submit", validators=[DataRequired()])

