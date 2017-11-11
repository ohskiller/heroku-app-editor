# webform/views.py

# IMPORTS
from flask import render_template, request, redirect, url_for, flash
from webform import app
from .forms import CodeForm

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def add_item():
    form = CodeForm(request.form)
    size = { 'left': 13, 'middle': 3, 'right': 3 }
    """Render homepage"""
    return render_template('code_entry.html', form=form, size=size)