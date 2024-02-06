from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange


class NumberForm(FlaskForm):
    numberField = IntegerField('Enter a number to check if it\'s prime:', validators=[InputRequired(message="You can't submit an empty response!"), NumberRange(min=0, message="Please provide positive integer")])
    submitField = SubmitField("Check primality!")