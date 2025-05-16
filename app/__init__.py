from flask import Flask
from flask import render_template
from random import Random
from datetime import date

app = Flask(__name__)

@app.get("/")
def root_home():
    return render_template("pages/home.jinja")


@app.get("/test/")
def root_test():
    return render_template("pages/test.jinja")

@app.get("/about/")
def root_about():
    return render_template("pages/about.jinja")

@app.get("/random/")
def root_random():
    dailyRandom = Random(date.today().strftime("%Y%M%D"))
    n = dailyRandom.randint(1, 1_000)
    return render_template("pages/random.jinja", number=n)

@app.errorhandler(404)
def root_404(error):
    return render_template("pages/errorCode.jinja",err=error)