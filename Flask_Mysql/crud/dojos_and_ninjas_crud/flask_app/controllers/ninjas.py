from flask import render_template, redirect, request, url_for
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/dojos/new_ninja")
def new_ninja():
    return render_template("new_ninja.html", all_dojos = Dojo.show_all())

@app.route("/dojos/create_ninja", methods = ["POST"])
def create_ninja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form["age"]
    }
    Ninja.create(data)
    return redirect("/dojos")
