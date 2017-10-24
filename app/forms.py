""" Forms file"""
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class AddcategoryForm(Form):
    """ Form"""
    categoryname = StringField('categoryname', validators=[DataRequired()])
    categorydescription = StringField(
        'categorydescription', validators=[DataRequired()])


class AddrecipeForm(Form):
    """ Form"""
    recipename = StringField('recipename', validators=[DataRequired()])
    recipeingredients = StringField(
        'recipeingredients', validators=[DataRequired()])
    recipedescription = StringField(
        'recipedescription', validators=[DataRequired()])
    recipecategory = StringField('recipecategory', validators=[DataRequired()])
    recipepicture = StringField('recipepicture', validators=[DataRequired()])


class EditcategoryForm(Form):
    """ Form"""
    categoryname = StringField('categoryname', validators=[DataRequired()])
    categorydescription = StringField(
        'categorydescription', validators=[DataRequired()])


class EditrecipeForm(Form):
    """ Form"""
    recipename = StringField('recipename', validators=[DataRequired()])
    recipeingredients = StringField(
        'recipeingredients', validators=[DataRequired()])
    recipedescription = StringField(
        'recipedescription', validators=[DataRequired()])
    recipecategory = StringField('recipecategory', validators=[DataRequired()])
    recipepicture = StringField('recipepicture', validators=[DataRequired()])
