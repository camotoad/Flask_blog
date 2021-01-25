from flaskblog import app
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm

@app.route("/")
@app.route("/home")
def home():
    # TODO homepage
    return render_template('home.html', title='Home')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # TODO account validation
        pass
    else:
        flash('Please check your username and password', 'danger')
    return render_template('login.html', title='login', form=form)