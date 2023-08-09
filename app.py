from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # Import for SQL Alchemy Database
from flask_migrate import Migrate, migrate # Import for Migrations

app = Flask(__name__)
app_debug = True;

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)


 
# Settings for migrations
migrate = Migrate(app, db)

@app.route("/")
def home():
    # return("heheh")
    return render_template('index.html')

# flask db migrate -m "Initial migration"