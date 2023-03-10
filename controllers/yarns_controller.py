from flask import Blueprint, render_template, request, redirect, flash
from repositories import yarn_repository, manufacturer_repository, colour_repository
from models.yarn import Yarn
from config.config import config

yarns_blueprint = Blueprint("yarns", __name__, url_prefix="/yarns")


@yarns_blueprint.route("/")
def yarns():
    yarns = yarn_repository.select_all()
    return render_template("/yarns/all.html", yarns=yarns)


@yarns_blueprint.route("/<id>")
def detail(id):
    yarn = yarn_repository.select(id)
    colours = colour_repository.select_by_yarn(id)
    return render_template("/yarns/detail.html", yarn=yarn, colours=colours)


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
        buy_cost = int(request.form.get("buy_cost", type=float) * 100)
        sell_price = int(request.form.get("buy_cost", type=float) * 100)

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
        )

        image = request.files["image"]
        new_yarn.save_image(image)
        yarn_repository.save(new_yarn)

        flash("Yarn added")
        return redirect("/yarns/")

    manufacturers = manufacturer_repository.select_all()
    return render_template(
        "/yarns/new.html", manufacturers=manufacturers, yarn_weights=yarn_weights
    )


@yarns_blueprint.route("/delete/<id>")
def delete_yarn(id):
    yarn_repository.delete(id)
    flash("Yarn deleted")
    return redirect("/yarns/")


@yarns_blueprint.route("/edit/<id>", methods=["GET", "POST"])
def edit_yarn(id):
    if request.method == "POST":
        name = request.form["name"]
        manufacturer = manufacturer_repository.select(request.form["manufacturer"])
        yarn_weight = request.form["yarn_weight"]
        ball_weight = int(request.form["ball_weight"])
        length = int(request.form["length"])
        needle_size = float(request.form["needle_size"])
        fibre_type = request.form["fibre_type"]
        buy_cost = int(request.form["buy_cost"].replace(".", ""))
        sell_price = int(request.form["sell_price"].replace(".", ""))

        yarn = Yarn(
            name,
            manufacturer,
            yarn_weight,
            ball_weight,
            length,
            needle_size,
            fibre_type,
            buy_cost,
            sell_price,
            id=id,
        )

        image = request.files["image"]
        if image:
            yarn.save_image(image)
        else:
            yarn.image = request.form["original_image"]

        yarn_repository.update(yarn)

        flash("Yarn updated")
        return redirect("/yarns/" + id)

    yarn = yarn_repository.select(id)
    manufacturers = manufacturer_repository.select_all()

    return render_template(
        "/yarns/edit.html",
        yarn=yarn,
        manufacturers=manufacturers,
        yarn_weights=config.user_data["yarn_weights"],
    )


@yarns_blueprint.route("/order/<colour_id>", methods=["POST"])
def order_stock(colour_id):
    colour = colour_repository.select(colour_id)

    quantity = int(request.form["quantity"])
    cost = colour.total_cost(quantity)

    colour.yarn.manufacturer.add_to_balance(cost)
    colour.increase_stock(quantity)

    colour_repository.update(colour)
    manufacturer_repository.update(colour.yarn.manufacturer)

    return redirect(request.referrer)
