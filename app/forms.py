from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class SigninForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class SignupForm(Form):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class AddcategoryForm(Form):
    categoryname = StringField('categoryname', validators=[DataRequired()])
    categorydescription = StringField('categorydescription', validators=[DataRequired()])

class AddrecipeForm(Form):
    recipename = StringField('recipename', validators=[DataRequired()])
    recipeingredients = StringField('recipeingredients', validators=[DataRequired()])
    recipedescription = StringField('recipedescription', validators=[DataRequired()])
    recipecategory = StringField('recipecategory', validators=[DataRequired()])
    recipepicture = StringField('recipepicture', validators=[DataRequired()])

class EditcategoryForm(Form):
    categoryname = StringField('categoryname', validators=[DataRequired()])
    categorydescription = StringField('categorydescription', validators=[DataRequired()])

class EditrecipeForm(Form):
    recipename = StringField('recipename', validators=[DataRequired()])
    recipeingredients = StringField('recipeingredients', validators=[DataRequired()])
    recipedescription = StringField('recipedescription', validators=[DataRequired()])
    recipecategory = StringField('recipecategory', validators=[DataRequired()])
    recipepicture = StringField('recipepicture', validators=[DataRequired()])

