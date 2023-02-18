from flask import Blueprint, render_template
from repositories import manufacturer_repository

manufacturers_blueprint = Blueprint(
    "manufacturers", __name__, url_prefix="/manufacturers"
)


@manufacturers_blueprint.route("/")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/show.html", manufacturers=manufacturers)
