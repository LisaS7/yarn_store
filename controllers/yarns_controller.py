from flask import Blueprint, render_template, request, redirect
from repositories import yarn_repository, manufacturer_repository
from models.yarn import Yarn
from config import yarn_weights

yarns_blueprint = Blueprint("yarns", __name__, url_prefix="/yarns")


@yarns_blueprint.route("/")
def yarns():
    yarns = yarn_repository.select_all()
    return render_template("/yarns/all.html", yarns=yarns)


@yarns_blueprint.route("/<id>")
def detail(id):
    yarn = yarn_repository.select(id)
    return render_template("/yarns/detail.html", yarn=yarn)


@yarns_blueprint.route("/new", methods=["GET", "POST"])
def create_yarn():
    if request.method == "POST":
        name = request.form["name"]
        manufacturer = manufacturer_repository.select(request.form["manufacturer"])
        yarn_weight = request.form["yarn_weight"]
        ball_weight = int(request.form["ball_weight"])
        length = int(request.form["length"])
        needle_size = float(request.form["needle_size"])
        fibre_type = request.form["fibre_type"]
        buy_cost = int(request.form["buy_cost"])
        sell_price = int(request.form["sell_price"])

        image = request.files["image"]
        Yarn.save_image(image)

        new_yarn = Yarn(
            name,
            manufacturer,
            yarn_weight,
            ball_weight,
            length,
            needle_size,
            fibre_type,
            buy_cost,
            sell_price,
            image.filename,
        )
        yarn_repository.save(new_yarn)
        return redirect("/yarns/")

    manufacturers = manufacturer_repository.select_all()
    return render_template(
        "/yarns/new.html", manufacturers=manufacturers, yarn_weights=yarn_weights
    )
