from flask import Flask

app = Flask(__name__)

fake_db = {
    "home":"home",
    "back":"back",
}

@app.route("/welcome")
def welcome():
    return "welcome"


@app.route("/welcome/<input>")
def welcome_inp(input):
    return f"welcome {input}"




