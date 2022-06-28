from flask import render_template, url_for, flash, redirect
from pulse import app, DB
from pulse.forms import EnterIncomeForm, AllocateIncomeForm

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/enter-income", methods=['GET','POST'])
def enter_income():
    form = EnterIncomeForm()
    if form.validate_on_submit():
        income = float(form.income.data)
        print(income)
        db = DB.read()
        db['income'] = income
        DB.write(db)
        flash('done','success')
        return redirect(url_for('allocate_income'))
    return render_template('enter-income.html', form=form)

@app.route("/allocate-income", methods=['GET','POST'])
def allocate_income():
    db = DB.read()
    income = db['income']
    form = AllocateIncomeForm()
    return render_template('allocate-income.html', income=income, form=form)

