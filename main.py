from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    events = [
        {
            "name":"Math test",
            "course":"MA162",
            "professor":"Glubokov",
        },
    ]
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
    app.run(host="0.0.0.0", port=8000, debug=True)
