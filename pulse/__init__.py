from fileinput import filename
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)
class DB:
    def read():
        with open('pulse/db.txt', 'r') as f:
            return eval(f.read())
    def write(db):
        with open('pulse/db.txt', 'w') as f:
            f.write(str(db))



from pulse import routes
