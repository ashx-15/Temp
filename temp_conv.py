# a temperature conversion app
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    converted_t = None
    temp = None
    if request.method== "POST":
        temp = int(request.form["temp"])
        converted_t = (temp-32)*0.5556
    return render_template("index.html", converted_t=converted_t, temp=temp)
