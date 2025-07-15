from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)

with app.app_context():
    if not os.path.exists("users.db"):
        db.create_all()

@app.route("/")
def index():
    return redirect(url_for("form"))

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        db.session.add(User(name=name, email=email))
        db.session.commit()
        return redirect(url_for("thankyou"))
    return render_template("form.html")

@app.route("/async-form", methods=["GET", "POST"])
def async_form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        from celery_app import save_user_async
        save_user_async.delay(name, email)
        return redirect(url_for("thankyou_async"))
    return render_template("async_form.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

@app.route("/thankyou_async")
def thankyou_async():
    return render_template("thankyou_async.html")

if __name__ == "__main__":
    app.run(debug=True)

