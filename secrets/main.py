from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import email_validator


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class LoginForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired(), Email(message="You must enter an email!")])
    password = PasswordField(label="Password", validators=[Length(min=8)] )
    submit = SubmitField(label="Log in")


app = Flask(__name__)
app.secret_key = "MySecretKey"


@app.route("/")

def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    my_form = LoginForm()
    if my_form.validate_on_submit():
        if my_form.name.data == "admin@email.com" and my_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    # custom_attrs = [v for v in vars(LoginForm().) if v not in any([vars(FlaskForm)])]
    return render_template('login.html', form=my_form, e_name=my_form.name.errors, e_pass=my_form.password.errors)

if __name__ == '__main__':
    app.run(debug=True)
