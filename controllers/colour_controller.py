from collections import defaultdict
from flask import Blueprint, render_template, request, redirect, flash
from repositories import colour_repository, yarn_repository
from models.colour import Colour

colours_blueprint = Blueprint("colours", __name__, url_prefix="/colours")


@colours_blueprint.route("/")
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


@colours_blueprint.route("/new/", methods=["GET", "POST"])
@colours_blueprint.route("/new/<yarn_id>", methods=["GET", "POST"])
def create_colour(yarn_id):

    yarn = yarn_repository.select(yarn_id)

    if request.method == "POST":
        print(request.form)
        name = request.form["name"]
        hex_code = request.form["colour"]
        quantity = int(request.form["quantity"])
        colour = Colour(name, hex_code, quantity, yarn)
        colour_repository.save(colour)
        flash("Colour added!")
        if request.form.get("submit-another"):
            return redirect(f"/colours/new/{yarn_id}")
        return redirect("/colours/")

    return render_template("/colours/new.html", yarn=yarn)


@colours_blueprint.route("/delete/<id>")
def delete(id):
    colour_repository.delete(id)
    flash("Colour deleted!")
    return redirect("/colours/")


@colours_blueprint.route("/edit/<id>", methods=["GET", "POST"])
def edit_colour(id):
    if request.method == "POST":
        yarn = yarn_repository.select(request.form["yarn"])
        name = request.form["name"]
        hex_code = request.form["colour"]
        quantity = int(request.form["quantity"])

        colour = Colour(name, hex_code, quantity, yarn, id)
        colour_repository.update(colour)
        flash("Colour updated")
        return redirect("/colours/")

    colour = colour_repository.select(id)
    yarns = yarn_repository.select_all()
    return render_template("/colours/edit.html", colour=colour, yarns=yarns)
