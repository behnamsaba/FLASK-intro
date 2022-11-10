from flask import Flask,request
import operations
app = Flask(__name__)
@app.route("/")
def root():
    return "<html><h3>Welcome to calculator server</h3></html>"

@app.route("/add")
def add():
    query_string = request.args.to_dict()
    a = query_string.get("a")
    b = query_string.get("b")
    
    return f"{operations.add(int(a),int(b))}"

@app.route("/sub")
def sub():
    query_string = request.args.to_dict()
    a = query_string.get("a")
    b = query_string.get("b")
    return f"{operations.sub(int(a),int(b))}"

@app.route("/mult")
def mult():
    query_string = request.args.to_dict()
    a = query_string.get("a")
    b = query_string.get("b")
    return f"{operations.mult(int(a),int(b))}"

@app.route("/div")
def div():
    query_string = request.args.to_dict()
    a = query_string.get("a")
    b = query_string.get("b")
    return f"{operations.div(int(a),int(b))}"





