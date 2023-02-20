from collections import defaultdict
from flask import Blueprint, render_template, request, redirect
from repositories import colour_repository, yarn_repository
from models.colour import Colour

colour_blueprint = Blueprint("colours", __name__, url_prefix="/colours")


@colour_blueprint.route("/")
def colours():
    yarn_groups = defaultdict(list)
    colours = colour_repository.select_all()

    for colour in colours:
        yarn_groups[colour.yarn.manufacturer.name + " - " + colour.yarn.name].append(
            colour
        )
    return render_template(
        "/colours/all.html", colours=colours, yarn_groups=yarn_groups
    )


@colour_blueprint.route("/new", methods=["GET", "POST"])
def create_colour():
    if request.method == "POST":
        name = request.form["name"]
        hex_code = request.form["colour"]
        quantity = request.form["quantity"]
        yarn = yarn_repository.select(request.form["yarn"])
        colour = Colour(name, hex_code, quantity, yarn)
        colour_repository.save(colour)
        return redirect("/colours/")
    yarns = yarn_repository.select_all()
    return render_template("/colours/new.html", yarns=yarns)


@colour_blueprint.route("/delete/<id>")
def delete(id):
    colour_repository.delete(id)
    return redirect("/colours/")
