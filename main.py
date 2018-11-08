from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)


@app.route("/js")
def js():
    return render_template("js.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)


@app.route("/shopping")
def shopping():
    food = ["Cheese", "Tuna", "Beef", "Toothpaste"]
    return render_template("shopping.html", food=food)


@app.route("/bacon", methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "you are using POST"
    else:
        return "you are probably using GET"


if __name__ == "__main__":
    app.run(debug=True)
