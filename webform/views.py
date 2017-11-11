# webform/views.py

# IMPORTS
from flask import render_template, request, redirect, url_for, flash
from webform import app
from .forms import CodeForm

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def publish_code():
    form = CodeForm(request.form)
    size = { 'left': 13, 'middle': 3, 'right': 3 }
    run = request.method == 'POST'
    if run: print('ran')
    """Render code form"""
    return render_template('code_entry.html', form=form, size=size, run=run)