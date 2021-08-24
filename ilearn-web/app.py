from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/goal", methods=["GET", "POST"])
# def goal():
#     goal = request.form.get("goal")

#     return render_template("goal.html", goal=goal)

@app.route("/climatechange")
def climatechange():
    return render_template("climatechange.html")


@app.route("/machinelearning")
def machinelearning():
    return render_template("machinelearning.html")


@app.route("/personalfinance")
def personalfinance():
    return render_template("personalfinance.html")

if __name__ == "__main__":
    app.run(debug=True)