from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def first_checkerboard():
    return render_template("index.html")

@app.route("/<x>/<y>")
def second_checkboard(x,y):
    x = int(x)
    y = int(y)
    return render_template("index.html", x = x, y=y)

if __name__=="__main__":
    app.run(debug = True)
