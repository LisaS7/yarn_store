from flask import Blueprint, render_template
from repositories import manufacturer_repository

manufacturers_blueprint = Blueprint(
    "manufacturers", __name__, url_prefix="/manufacturers"
)


@manufacturers_blueprint.route("/")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/all.html", manufacturers=manufacturers)


@manufacturers_blueprint.route("/<id>")
def detail(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("/manufacturers/detail.html", manufacturer=manufacturer)
