from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

# Start app, and add bootstrap and moment functionalities
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# Add secret key required for WTF configuration
app.config['SECRET_KEY'] = 'hard to guess string'

# Create a form class
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Define template rendering for root route
@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name, current_time=datetime.now())

# Define template rendering for user route with variable handling
@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name, current_time=datetime.now())

# Define template rendering for HTML error 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Define template rendering for HTML error 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500