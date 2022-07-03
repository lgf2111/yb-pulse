from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, IntegerField, SelectField, DateField, StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from pulse import DB
from datetime import datetime


class EnterIncomeForm(FlaskForm):
    income = DecimalField('Enter Your Income', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class AllocateIncomeForm(FlaskForm):
    savings = IntegerField('Savings', default=0)
    invest = IntegerField('Invest', default=0)
    shopping = IntegerField('Shopping', default=0)
    food_and_health = IntegerField('Food & Health', default=0)
    lifestyle = IntegerField('Lifestyle', default=0)
    bills = IntegerField('Bills', default=0)
    others = IntegerField('Others', default=0)
    submit = SubmitField('Next')
    
class AddExpenseForm(FlaskForm):
    db = DB.read()
    manual = ["Savings","Invest","Shopping","Food & Health","Lifestyle","Bills","Others"]
    name = StringField('NAME', validators=[DataRequired()])
    category = SelectField('CATEGORY', choices=db['allocation'].keys() if db.get('allocation') else manual)
    amount = DecimalField('AMOUNT', validators=[DataRequired()])
    date = DateField('DATE', validators=[DataRequired()], default=datetime.today)
    invoice = FileField('INVOICE', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Next')