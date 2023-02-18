from flask import Blueprint, render_template, request, redirect
from repositories import manufacturer_repository
from models.manufacturer import Manufacturer
from datetime import datetime as dt

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


@manufacturers_blueprint.route("/new", methods=["GET", "POST"])
def create_manufacturer():
    if request.method == "POST":
        name = request.form["name"]
        balance_due = request.form["balance_due"]

        last_payment_date = request.form["last_payment_date"]
        year, month, day = map(int, last_payment_date.split("-"))

        new_manufacturer = Manufacturer(name, dt(year, month, day), balance_due)
        manufacturer_repository.save(new_manufacturer)
        return redirect("/manufacturers/")
    return render_template("/manufacturers/new.html")


@manufacturers_blueprint.route("/delete/<id>")
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers/")
