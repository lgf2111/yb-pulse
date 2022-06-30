from fileinput import filename
from flask import render_template, url_for, flash, redirect
from pulse import app, DB
from pulse.forms import EnterIncomeForm, AllocateIncomeForm, AddExpenseForm
from pulse.utils import generate_analysis_report, save_picture

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/enter-income", methods=['GET','POST'])
def enter_income():
    form = EnterIncomeForm()
    if form.validate_on_submit():
        income = float(form.income.data)
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
    if form.validate_on_submit():
        savings = form.savings.data
        invest = form.invest.data
        shopping = form.shopping.data
        food_and_health = form.food_and_health.data
        lifestyle = form.lifestyle.data
        bills = form.bills.data
        others = form.others.data
        allocation =   {'Savings': savings,
                        'Invest': invest,
                        'Shopping': shopping,
                        'Food & Health': food_and_health,
                        'Lifestype': lifestyle,
                        'Bills': bills,
                        'Others': others,
                        }
        for cat in allocation:
            if not cat:
                allocation[cat] = 0
            allocation[cat] = float(allocation[cat])
        db = DB.read()
        db['allocation'] = allocation
        DB.write(db)
        flash('done', 'success')
        return redirect(url_for('analysis_report'))
    return render_template('allocate-income.html', income=income, form=form)

@app.route("/analysis-report")
def analysis_report():
    db = DB.read()
    allocation = db['allocation']
    report = generate_analysis_report(allocation)
    return render_template('analysis-report.html', report=report)

@app.route("/home")
def home():
    db = DB.read()
    card = db['card']
    income = db['income']
    allocation = db['allocation']
    categories = [(k,income * v / 100) for k,v in allocation.items()]
    categories.sort(key=lambda x: x[1], reverse=True)
    return render_template('home.html', card=card, categories=categories)

@app.route("/add-expense", methods=['GET','POST'])
def add_expense():
    form = AddExpenseForm()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        amount = float(form.amount.data)
        date = form.date.data.strftime(r"%d/%m/%Y")
        invoice = save_picture(form.invoice.data)
        expense =  {'name': name,
                    'category': category,
                    'amount': amount,
                    'date': date,
                    'invoice': invoice}
        db = DB.read()
        if not db.get('expenses'):
            db['expenses'] = []
        db['expenses'].append(expense)
        DB.write(db)
        return(redirect(url_for('transactions_history')))

    return render_template('add-expense.html', form=form)

@app.route("/transactions-history")
def transactions_history():
    db = DB.read()
    expenses = db['expenses']
    total = sum(map(lambda x: x['amount'], expenses))
    return render_template('transactions-history.html', expenses=expenses, total=total)