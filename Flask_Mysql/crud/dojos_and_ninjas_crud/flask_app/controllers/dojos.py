from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

#Path to index
@app.route("/dojos")
def index():
    return render_template("index.html", all_dojos = Dojo.show_all())

#Path to create new dojo/posts it on same page
@app.route("/dojos", methods= ["POST"])
def new_dojo():
    Dojo.new_dojo(request.form)
    return render_template("index.html", all_dojos = Dojo.show_all())

#Path to display individual dojo, with associated ninjas
@app.route("/dojos/<int:dojo_id>")
def display_dojo(dojo_id):
    return render_template("dojo_members.html", dojo = Dojo.display_dojo({"id": dojo_id}))