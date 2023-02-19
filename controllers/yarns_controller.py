from flask import Blueprint, render_template, request, redirect
from repositories import yarn_repository
from models.yarn import Yarn

yarns_blueprint = Blueprint("yarns", __name__, url_prefix="/yarns")


@yarns_blueprint.route("/")
def yarns():
    yarns = yarn_repository.select_all()
    return render_template("/yarns/all.html", yarns=yarns)


@yarns_blueprint.route("/<id>")
def detail(id):
    yarn = yarn_repository.select(id)
    return render_template("/yarns/detail.html", yarn=yarn)
