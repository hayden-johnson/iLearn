from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/goal", methods=["GET", "POST"])
def goal():
    goal = request.form.get("goal")

    return render_template("goal.html", goal=goal)

if __name__ == "__main__":
    app.run(debug=True)