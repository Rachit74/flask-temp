from flask import Blueprint, render_template, request,flash, redirect, url_for
from .models import User
from werkzeug.security import check_password_hash, generate_password_hash
from . import db,views
from flask_login import login_user, login_required, current_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                global login
                login_user(user,remember=True)
                flash("Logged in!")
            else:
                flash("Wrong Password")
                login = False
        else:
            flash("wrong email")


    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        password_c = request.form.get("password_c")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("User Alredy Exists!")

        if len(email) < 4:
            flash("short Email", category='e')
        elif len(name) < 2:
            flash("short Name", category='e')
        elif password != password_c:
            flash("Password No Match", category='e')
        elif len(password) < 8:
            flash("short password", category='e')
        else:
            user = User(email=email,name=name,password=password)
            db.session.add(user)
            db.session.commit()
            flash("Created", category='s')
            login_user(user,remember=True)
            redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)