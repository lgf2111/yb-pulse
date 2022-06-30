from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, IntegerField, SelectField, DateField, StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from pulse import DB


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
    
class AddExpenseForm(FlaskForm):
    db = DB.read()
    name = StringField('NAME')
    category = SelectField('CATEGORY', choices=db['allocation'].keys())
    amount = DecimalField('AMOUNT')
    date = DateField('DATE')
    invoice = FileField('INVOICE', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Next')