#flask #forms

## Benefits of flask-wtf (flask extension)
* easy form validation
* Less code
* built in CSRF (Cross Site Request Forgery) protection. 

## [Flask-WTF docs](https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/)
## Project goal:
* Build a website that holds some secrets and require user authentication to access them.

## build venv from `requirements.txt`:
* `pip install -r requirements.txt`
* should have created a venv folder

## Creating forms with Flask-WTF:
### Login Form Requirements:
1. Must have an `email` and `password` field.
2. Both fields can be `StringFields`
   * If you make password a `PasswordField` it will obscure entered text
   * You can use a `SubmitField` instead of `input type="submit"`
3. Don't worry about `validators`
4. set both inputs to `size 30`

## Making the forms
```python
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
```
```html
<form method="POST" action="/">
    {{ form.csrf_token }}
    {{ form.name.label }} {{ form.name(size=20) }}
    <input type="submit" value="Go">
</form>
```

## main.py
```python
class LoginForm(FlaskForm):
    name = StringField(label="Name")


app = Flask(__name__)


@app.route("/")

def home():
    return render_template('index.html')


@app.route("/login")
def login():
    my_form = LoginForm(meta={'csrf': False})
    return render_template('login.html', form=my_form)
```

## Adding CSRF protection:
* put `{{ form.csrf token }}` in HTML
* create secret key in main.py: `app.secret_key = "the secret"`

## Adding validation to forms
* Add validator objects when we create each field in our form
* Don't forget to `validate_on_submit()`
* Our validation wont work unless we turn off browser validation. This is accomplished with a `"novalidate"` attribute
on the form element in our HTML.
## Receiving data with flask-wtf
* entered data lives in `<form_object>.<form_name>.data`

## Inheriting templates using Jinja
* Use template inheritance when you want to use the same design template for your entire website but only want
to change some code in your header or footer.
* create a `base.html`
* ```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>{% block title %}{% endblock %}</title>
</head>
<body>
   {% block content %}{% endblock %}
</body>
</html>
```

The above has blocks  where new content can be inserted by a child webpage inheriting from this template

### We could re-write `success.html` to inherit from `base.html`
#### success.html
```html
{% extends "base.html" %}<!-- Tells Jinja to use base.html as the template for this page -->
{% block title %}Success{% endblock %}<!-- Inserts a custom title into template header -->
{% block content %}<!-- Provides the content of the website: the part that is going to vary between webpages. -->
    <div class="container">
       <h1>Top Secret</h1>
       <iframe src="https://giphy.com/embed/Ju715y9osyymQ" width="480" height="360" frameBorde="0" class="giphy-embed" allowfullscreen></iframe>
       <p><a href="https://giphy.com/gifs/rick-astley-Ju715y9osyymQ">via GIPHY</a></p>
    </div>
{% endblock %}
```

### super blocks
* We can use super blocks when there's some part of the template that we want to keep, but we also want to add to it
* You have a styling block in your base template that all other pages inherit, but you want to give special styling to
on page in particular. However, the `<style>` tag is in your base.html template. This is what super blocks are for.
```html
{% block styling %} {{ super() }} {% endblock %}
h1 {
color: red;
}
{% endblock %}
```
This injects all  the code from the styling block in base.html, allowing you to add code without overriding it. 