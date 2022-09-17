from pydoc import describe
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = "very secret"

db = SQLAlchemy(app)

class Events(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    assignment = db.Column(db.String(200)
    professor = db.Column(db.String(200))
    code = db.Column(db.String(6))
    location = db.Column(db.String(2000))
    date = db.Column(db.DateTime(400))
    description = db.Column(db.String(300))

    def __init__( self , assignment , professor , code , description ):
        self.assignment = assignment
        self.professor = professor
        self.code = code 
        self.description = description
        self.location = location
        self.dateTime = dateTime


@app.route('/', methods=["GET", "POST"])
def index():
    events = Events.query.all()
    if request.method == 'POST':
        form_data = request.form
        assignment = form_data['assignment']
        code = form_data['code']
        professor = form_data['professor']
        dateTime = form_data['Date and Time of Meeting']
        description = form_data['description']
        location = form_data['location']
        event = Events(assignment, professor, code, dateTime, description , location)
        description = form_data['description']
        event = Events(assignment, professor, code, description)
        db.session.add(event)
        db.session.commit()
        return 

    return render_template('index.html', events=events)





if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", port=8000, debug=True)

