from flask import Blueprint, render_template, request
from helper_functions.json_functions import read_user_config, write_user_config

settings_blueprint = Blueprint("settings", __name__, url_prefix="/settings")


@settings_blueprint.route("/", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        output = request.form

        yarn_weights = [
            output[item]
            for item in output
            if item.startswith("yarn_weight") and output[item] != ""
        ]

        data = {
            "low_stock_threshold": output["low_stock_threshold"],
            "yarn_weights": yarn_weights,
        }

        write_user_config(data)

    data = read_user_config()
    context = {
        "low_stock": data["low_stock_threshold"],
        "yarn_weights": data["yarn_weights"],
    }
    return render_template("/settings/index.html", context=context)
