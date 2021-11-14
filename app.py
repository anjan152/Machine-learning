from flask import Flask, render_template

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/registration")
def registration():
    return render_template("registration.html")
@app.route("/upload")
def upload():
    return render_template("upload.html")