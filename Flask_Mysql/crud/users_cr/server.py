from flask import Flask, render_template
from mysqlconnection import connectToMySQL
app=Flask(__name__)

@app.route("/")
def index()



if __name__=="__main__":
    app.run(debug=True)
