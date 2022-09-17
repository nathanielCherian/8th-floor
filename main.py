from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = "very secret"

db = SQLAlchemy(app)

class Events(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    assignment = db.Column(db.String(200))
    professor = db.Column(db.String(200))
    course =db.Column(db.String(200))
    # dueDate = db.Column(db.String(200))
    def __init__( self , assignment , professor , code  ):
        self.assignment = assignment
        self.professor = professor
        self.code = code 

@app.route('/', methods=["GET", "POST"])
def index():
    events = Events.query.all()
    if request.method == 'POST':
        form_data = request.form
        assignment = form_data['assignment']
        code = form_data['code']
        professor = form_data['professor']
        event = Events(assignment, professor, code)
        db.session.add(event)
        db.session.commit()

    return render_template('index.html', events=events)

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route('/create-account', methods=['POST', 'GET'])
def create_account():
    return render_template("create_account.html")

@app.route("/api/create-event", methods=['POST'])
def create_event():
    return

@app.route("/api/get-event", methods=['GET'])
def get_events():
    return {}



if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", port=8000, debug=True)

