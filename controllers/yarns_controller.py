from flask import Blueprint, render_template, request, redirect
from repositories import yarn_repository
from models.yarn import Yarn

yarns_blueprint = Blueprint("yarns", __name__, url_prefix="/yarns")


@yarns_blueprint.route("/")
def yarns():
    yarns = yarn_repository.select_all()
    print(yarns)
    return render_template("/yarns/all.html", yarns=yarns)
