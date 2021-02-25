from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, flash, redirect, url_for
from forms import LoginForm
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    user = {'username': 'Kenny'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route("/login",  methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me{}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title="Sing In", form=form)


