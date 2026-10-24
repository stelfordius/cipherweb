from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
	return render_template("pages/home.html")

@bp.route("/week_1")
def week_1():
	return render_template("pages/week_1.html")
