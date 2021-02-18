from flask import Flask, render_template, render_template, flash, redirect
import cgi, cgitb



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/comparisson")
def comparisson():
    return render_template("comparisson.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/temperature")
def temperature():
    return render_template("maxTemp.html")

@app.route("/humidity")
def humidity():
    return render_template("humidity.html")

@app.route("/cloudiness")
def cloudiness():
    return render_template("cloudiness.html")

@app.route("/windSpeed")
def windSpeed():
    return render_template("windSpeed.html")


if __name__ == "__main__":
    app.run(debug=True)