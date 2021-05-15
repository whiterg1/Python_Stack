from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app=Flask(__name__)

@app.route("/users")
def index():
    mysql = connectToMySQL("users_schema")
    query = "SELECT * FROM users;"
    users = mysql.query_db(query)
    return render_template("Read(all).html", all_users = users)


@app.route("/users/new")
def new_user_form():
    return render_template("Create.html")

@app.route("/users/create", methods = ["POST"])
def new_user():
    mysql = connectToMySQL("users_schema")
    query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) \
    VALUES(%(first_name)s,%(last_name)s,%(email)s,NOW(), NOW());"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    user_id = mysql.query_db(query, data)
    
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)
