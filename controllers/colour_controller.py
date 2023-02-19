from flask import Blueprint, render_template, request, redirect
from repositories import colour_repository

colour_blueprint = Blueprint("colours", __name__, url_prefix="/colours")


@colour_blueprint.route("/")
def colours():
    colours = colour_repository.select_all()
    return render_template("/colours/all.html", colours=colours)


@colour_blueprint.route("/delete/<id>")
def delete(id):
    colour_repository.delete(id)
    return redirect("/colours/")
