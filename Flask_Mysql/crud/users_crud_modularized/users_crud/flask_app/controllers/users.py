from flask import render_template, redirect, request
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

@app.route("/users")
def index():
    return render_template("Read(all).html", all_users = User.show_all())

@app.route("/users/new")
def new_user_form():
    return render_template("Create.html")

@app.route("/users/create", methods = ["POST"])
def new_user():
    User.save(request.form)
    return render_template("/users")

@app.route("/users/<int:user_id>")
def show_user(user_id):
    data = {
        "id": user_id
    }
    return render_template("Read(One).html", user = User.show_by_id(data))

@app.route("/users/<int:user_id>/edit")
def edit_user_form(user_id):
    data ={
        "id": user_id
    }
    return render_template("Edit_User.html", user = User.show_by_id(data))

@app.route("/users/<int:user_id>/update", methods = ['POST'])
def update_user(user_id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": user_id
    }
    User.update(data)
    return redirect("/users")

@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    data = {
        "id": user_id
    }
    User.delete(data)
    return redirect("/users")