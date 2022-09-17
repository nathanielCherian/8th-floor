from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = "very secret"

db = SQLAlchemy(app)


@app.route('/', methods=["GET", "POST"])
def index():
    events = [
        {
            "name":"Math test",
            "course":"MA162",
            "professor":"Glubokov",
        },
    ]

    if request.method == 'POST':
        form_data = request.form
        name = form_data['class_name']
        events.append({
            "name":name,
            "course":'test',
            "professor":"test"
        })
        print(name)

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

