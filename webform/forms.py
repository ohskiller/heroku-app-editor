from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, StringField
from wtforms.validators import DataRequired, Length, EqualTo, Email

content = [
"""import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)""",

"""Flask==0.7.2""",

"""web: python app.py"""
]

class CodeForm(FlaskForm):
    left = TextAreaField('app.py', default=content[0])
    middle = TextAreaField('requirements.txt', default=content[1])
    right = TextAreaField('Procfile', default=content[2])