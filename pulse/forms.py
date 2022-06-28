from sre_parse import CATEGORIES
from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired


class EnterIncomeForm(FlaskForm):
    income = DecimalField('Enter Your Income', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class AllocateIncomeForm(FlaskForm):
    savings = IntegerField('Savings', validators=[DataRequired()])
    invest = IntegerField('Invest', validators=[DataRequired()])
    shopping = IntegerField('Shopping', validators=[DataRequired()])
    food_and_health = IntegerField('Food & Health', validators=[DataRequired()])
    lifestyle = IntegerField('Lifestyle', validators=[DataRequired()])
    bills = IntegerField('Bills', validators=[DataRequired()])
    others = IntegerField('Others', validators=[DataRequired()])
    submit = SubmitField('Next')
    