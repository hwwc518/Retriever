#forms.py
from flask import Flask
from wtforms import Form, StringField, SelectField

class objSearchForm(Form):
    choices = [('Object', 'Zipcode')]
    select = SelectField('Search for an item:', choices=choices)
    search = StringField('')
