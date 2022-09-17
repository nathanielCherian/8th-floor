from flask import Flask, render_template, request

app = Flask(__name__)


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
    if request.method == 'POST':

    return

@app.route("/api/get-event", methods=['GET'])
def get_events():
    return {}



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
