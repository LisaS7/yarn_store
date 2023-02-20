from flask import Flask, render_template
from controllers.manufacturers_controller import manufacturers_blueprint
from controllers.yarns_controller import yarns_blueprint
from controllers.colour_controller import colours_blueprint

app = Flask(__name__)
app.register_blueprint(manufacturers_blueprint)
app.register_blueprint(yarns_blueprint)
app.register_blueprint(colours_blueprint)
app.secret_key = "This Is Top Secret"


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
