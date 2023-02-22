from flask import Blueprint, render_template, request, redirect, flash
from repositories import manufacturer_repository, yarn_repository
from models.manufacturer import Manufacturer

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
    yarns = yarn_repository.select_by_manufacturer(id)
    return render_template(
        "/manufacturers/detail.html", manufacturer=manufacturer, yarns=yarns
    )


@manufacturers_blueprint.route("/new", methods=["GET", "POST"])
def create_manufacturer():
    if request.method == "POST":
        name = request.form["name"]
        balance_due = int(request.form.get("balance_due", type=float) * 100)
        last_payment_date = Manufacturer.form_date_to_datetime(
            request.form["last_payment_date"]
        )

        new_manufacturer = Manufacturer(name, last_payment_date, balance_due)
        manufacturer_repository.save(new_manufacturer)

        flash("Manufacturer added")
        return redirect("/manufacturers/")
    return render_template("/manufacturers/new.html")


@manufacturers_blueprint.route("/delete/<id>")
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    flash("Manufacturer deleted")
    return redirect("/manufacturers/")


@manufacturers_blueprint.route("/edit/<id>", methods=["GET", "POST"])
def edit_manufacturer(id):
    if request.method == "POST":
        name = request.form["name"]
        balance_due = int(request.form["balance_due"].replace(".", ""))

        last_payment_date = Manufacturer.form_date_to_datetime(
            request.form["last_payment_date"]
        )

        manufacturer = Manufacturer(name, last_payment_date, balance_due, id)
        manufacturer_repository.update(manufacturer)
        flash("Manufacturer updated")
        return redirect("/manufacturers/")

    manufacturer = manufacturer_repository.select(id)
    return render_template("/manufacturers/edit.html", manufacturer=manufacturer)
