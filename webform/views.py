# webform/views.py

# IMPORTS
import os
import shutil
from flask import render_template, request, redirect, url_for, flash
from webform import app
from .forms import CodeForm
from pyutils_rdm import push_from_site_to_heroku, write_lines_to_file

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def publish_code():
    push_data = []
    form = CodeForm(request.form)
    size = { 'left': 13, 'middle': 3, 'right': 3 }
    run = False
    if request.method == 'POST':
        run = True
        try:
            shutil.rmtree('tmp')
        except:
            pass
        os.makedirs('tmp')
        for field in [form.left, form.middle, form.right]:
            write_lines_to_file('tmp/' + field.label.text, str(field.data).split('\n'))
        push_data = push_from_site_to_heroku('tmp', 'my-tiny-heroku-app')
    """Render code form"""
    return render_template('code_entry.html', form=form, size=size, run=run, push_data=push_data)