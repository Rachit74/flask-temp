from flask import Blueprint, render_template, request,flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET","POST"])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return '<h1>logout</h1>'

@auth.route('/signup', methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        password_c = request.form.get("password_c")

        if len(email) < 4:
            flash("short Email", category='e')
        elif len(name) < 2:
            flash("short Name", category='e')
        elif password != password_c:
            flash("Password No Match", category='e')
        elif len(password) < 8:
            flash("short password", category='e')
        else:
            flash("Created", category='s')

    return render_template("signup.html")