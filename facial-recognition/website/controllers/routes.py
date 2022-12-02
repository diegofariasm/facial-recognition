from flask import Blueprint, render_template
from flask_login import login_required, current_user

routes = Blueprint("routes", __name__)


@routes.route("/")
@login_required
def home():
    return render_template("index.jinja", user=current_user)

@routes.route("/attendance")
@login_required
def attendance():
    return render_template("attendance.jinja", user=current_user)