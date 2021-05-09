from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play/<boxes>")
def box_multiplier(boxes):
    boxes = int(boxes)
    return render_template("index2.html", repeat=boxes)

@app.route("/play/<boxes>/<color_change>")
def box_color(boxes,color_change):
    boxes = int(boxes)
    new_color = color_change
    return render_template("index3.html",repeat=boxes, new_color=color_change)

if __name__=="__main__":
    app.run(debug=True)

