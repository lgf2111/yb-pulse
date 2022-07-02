from fileinput import filename
from flask import Flask
import json
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)
class DB:
    def read():
        try:
            with open('pulse/db.json', 'r') as f:
                return json.load(f)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            with open('pulse/db.json', 'w') as f:
                json_data = {}
                json.dump(json_data, f)

    def write(db):
        with open('pulse/db.json', 'w') as f:
            json.dump(db, f, indent=4)



from pulse import routes
