from flask import Flask,render_template


app=Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")
@app.route("/list")
def listt ():
    return render_template("list.html")
@app.route("/recomendetion")
def recomendetion (man):
    return render_template("recomendetion.html",man=man)
