from pydoc import describe
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = "very secret"

db = SQLAlchemy(app)

class Events(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    assignment = db.Column(db.String(200))
    professor = db.Column(db.String(200))
    code = db.Column(db.String(6))
    location = db.Column(db.String(100))
    date = db.Column(db.DateTime())
    description = db.Column(db.String(300))

    email = db.Column(db.String(200))
    name = db.Column(db.String(200))

    rsvp = db.Column(db.Integer())

    def __init__( self , assignment , professor , code , location, date, description, email, name ):
        self.assignment = assignment
        self.professor = professor
        self.code = code 
        self.location = location
        self.date = date
        self.description = description

        self.email = email
        self.name = name

        self.rsvp = 0


@app.route('/', methods=["GET", "POST"])
def index():
    events = Events.query.all()
    if request.method == 'POST':
        form_data = request.form
        assignment = form_data['assignment']
        professor = form_data['professor']
        code = form_data['code']
        location = form_data['location']
        date = datetime.strptime(form_data['date'], '%Y-%m-%dT%H:%M')
        description = form_data['description']

        email = form_data['email']
        name = form_data['name']
        event = Events(assignment, professor, code, location, date, description, email, name)
        db.session.add(event)
        db.session.commit()
        return redirect("/")

    return render_template('index.html', events=events)


@app.route('/rsvp/<event_id>', methods=['GET'])
def rsvp(event_id):
    event_id = int(event_id)
    event = Events.query.get(event_id)
    event.rsvp += 1
    db.session.commit()
    return "yo"



if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", port=8000, debug=True)

