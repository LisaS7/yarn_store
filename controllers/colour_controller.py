from collections import defaultdict
from flask import Blueprint, render_template, request, redirect
from repositories import colour_repository

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


@colour_blueprint.route("/delete/<id>")
def delete(id):
    colour_repository.delete(id)
    return redirect("/colours/")
