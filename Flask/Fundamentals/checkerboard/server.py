from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def first_checkerboard():
    return render_template("index.html")

@app.route("/<int:x>")
def second_checkerboard(x):
    return render_template("index2.html", x = x)

@app.route("/<int:x>/<int:y>")
def third_checkboard(x,y):
    return render_template("index3.html", x = x, y = y)

if __name__=="__main__":
    app.run(debug = True)
