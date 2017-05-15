# ourapp/views.py

from flask import Blueprint, render_template, redirect, url_for

from .forms import EmailPasswordForm

user = Blueprint('user', __name__)

@user.route('/login', methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():

        # Check the password and log the user in
        # [...]

        return redirect(url_for('index'))

    return render_template('login.html', form=form)
