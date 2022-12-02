from flask import Blueprint, render_template
from flask_login import login_required, current_user

routes = Blueprint("routes", __name__)


@routes.route("/")
@login_required
def home():
    return render_template("index.html", user=current_user)