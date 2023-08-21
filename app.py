from flask import Flask, render_template, request, redirect
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

if __name__ == '__main__':
    app.run()

@app.route("/")
def home():
    return render_template('index.html')



class Breed (db.Model):
    Name = db.Column(db.String(20), primary_key=True)
    Price = db.Column(db.String(20), nullable=True)
    Size = db.Column(db.String(20), nullable=True)
    Activity = db.Column(db.Integer, nullable=True)
    Hair_length = db.Column(db.String(20), nullable=True)

@app.route('/add')
def add_data():
    return render_template('Add_Breed.html')

@app.route('/add', methods=["POST"])
def newprofile():

    name = request.form.get("name")
    size = request.form.get("size")
    hair = request.form.get("hair")
 
    # create an object of the Profile class of models
    # and store data as a row in our datatable
    if name != '' and size != '' and hair is not None:
        p = Breed(Name=name, Size=size, Hair_length=hair)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')

@app.route('/', methods=["POST"])
def profile():
    # This function will take the inputed user data
    social = request.form.get("social")
    price = request.form.get("price")
    size = request.form.get("size")
    vocal = request.form.get("vocal")
    print(size , "  size")
    receivedData = {'social':social,'price' :price, 'size': size, 'vocal':vocal}
    # create an object of the Profile class of models and
    # store data as a row in our datatable
    # data = Cat_Breed.query.filter_by(size = receivedData["size"]).all()
    # employees = Breed.query.filter_by(Size = "S")
    employees = Breed.query.all()
    print(employees , " reslt")
    return redirect('/')


# flask db migrate -m "Initial migration"
# flask db upgrade