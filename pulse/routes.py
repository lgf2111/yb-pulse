from flask import render_template, url_for, flash, redirect
from pulse import app, DB
from pulse.forms import EnterIncomeForm, AllocateIncomeForm, AddExpenseForm
from pulse.utils import generate_analysis_report, save_picture, create_card

@app.route("/")
@app.route("/home")
def home():
    db = DB.read()
    card = db['card'] if db.get('card') else create_card()
    income = db.get('income')
    if not income:
        flash('Please start by entering your income.', 'info')
        return redirect(url_for('enter_income'))
    allocation = db.get('allocation')
    # categories = [(k,income * v / 100) for k,v in allocation.items()] if allocation else []
    
    categories = {k:0 for k,_ in allocation.items()}
    expenses = db.get('expenses')
    if expenses:
        for expense in expenses:
            categories[expense['category']] += expense['amount']

    # categories.sort(key=lambda x: x[1], reverse=True)
    return render_template('home.html', card=card, categories=categories)

@app.route("/enter-income", methods=['GET','POST'])
def enter_income():
    form = EnterIncomeForm()
    if form.validate_on_submit():
        income = float(form.income.data)
        db = DB.read()
        db['income'] = income
        DB.write(db)
        return redirect(url_for('allocate_income'))
    return render_template('enter-income.html', form=form)

@app.route("/allocate-income", methods=['GET','POST'])
def allocate_income():
    db = DB.read()
    income = db['income'] if db.get('income') else 0
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
                        'Lifestyle': lifestyle,
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
        return redirect(url_for('analysis_report'))
    return render_template('allocate-income.html', income=income, form=form)

@app.route("/analysis-report")
def analysis_report():
    db = DB.read()
    allocation = db.get('allocation')
    report = generate_analysis_report(allocation)
    return render_template('analysis-report.html', report=report)

@app.route("/add-expense", methods=['GET','POST'])
def add_expense():
    form = AddExpenseForm()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        amount = float(form.amount.data)
        date = form.date.data.strftime(r"%d/%m/%Y")
        invoice = save_picture(form.invoice.data, default='invoice')
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
    expenses = db['expenses'] if db.get('expenses') else []
    total = sum(map(lambda x: x['amount'], expenses)) if expenses else 0
    return render_template('transactions-history.html', expenses=expenses, total=total)