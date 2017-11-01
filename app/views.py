""" Views file for the Flask APP"""
from flask import render_template, session, redirect, url_for, flash, request
from wtforms import Form, StringField, PasswordField, TextField, TextAreaField, validators
from functools import wraps
from app import APP
from .models.users import User

users = []


class RegisterForm(Form):
    """ create form input fields for register"""
    username = StringField('username',
                           [validators.Length(min=1, max=50)])
    email = TextField('email',
                      [validators.DataRequired(),
                          validators.Email()])
    bio = TextField('bio',
                    [validators.Length(min=1, max=255)])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('password_confirm',
                             message='password do not match'),
        validators.Length(min=6, max=25)])
    password_confirm = PasswordField('password_confirm')


class LoginForm(Form):
    """create from input field for login"""
    email = TextField('email', [
        validators.DataRequired(), validators.Email()])
    password = PasswordField('password',
                             [validators.DataRequired()
                              ])


class CreateCategory(Form):
    """create form input for category"""
    categorytitle = StringField('categorytitle', [validators.DataRequired()])
    categorydescription = StringField('categorydescription')


class EditCategory(Form):
    """create form input fields for edit"""
    categorytitle = StringField('newtitle', [validators.DataRequired()])
    categorydescription = StringField(
        'newdescription', [validators.DataRequired()])


class CreateRecipe(Form):
    """creates form input field for adding recipe"""
    recipetitle = StringField('recipetitle', [validators.DataRequired()])
    recipedescription = TextAreaField('recipedescription')


class EditRecipe(Form):
    """creates form input field for editing recipe"""
    recipetitle = StringField('newtitle', [validators.DataRequired()])
    recipedescription = StringField(
        'newdescription', [validators.DataRequired()])


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please login in first')
            return redirect(url_for('signin', next=request.url))
    return decorated_function

def provide_user():
    for user in users:
      if user.email == session['logged_in']:
          return user

@APP.route('/')
@APP.route('/index')
def index():
    """ Here the user sees the signup and signin gateways """
    return render_template('home.html',
                           title='Home')


@APP.route('/addcategory', methods=['GET', 'POST'])
@login_required
def addcategory():
    """ A form to add a new category """
    form = CreateCategory(request.form)
    currentuser = provide_user()
    error = None
    if request.method == 'POST' and form.validate():
        for user in users:
            if user.email == session['logged_in']:
                currentuser = user
                user.create_category(form.categorytitle.data,
                                     form.categorydescription.data
                                     )
                return redirect('/viewcategory')
            else:
                flash("You should login first")
    return render_template('addcategory.html',
                           title='addcategory',
                           form=form,
                           user=currentuser)


@APP.route('/addrecipe/<id>', methods=['GET', 'POST'])
@login_required
def addrecipe():
    """ A form that adds a new recipe """
    form = CreateRecipe(request.form)
    currentuser = provide_user()
    error = None
    if request.method == 'POST' and form.validate():
        for user in users:
            if user.email == session['logged_in']:
                currentuser = user
                for category in user.categories.values():
                    if id == category.id:
                        category.add_recipe(form.recipetitle.data, form.recipedescription.data)
                        return redirect('/viewrecipe')
            else:
                flash("You should login first")
    return render_template('addrecipe.html',
                           title='addrecipe',
                           user=currentuser)


@APP.route('/category/<id>', methods=['GET', 'POST'])
@login_required
def category():
    """ This is a view page for the category """
    currentuser = provide_user()
    return render_template('category.html',
                           title='category',
                           user=currentuser)


@APP.route('/editcategory', methods=['GET', 'POST'])
@login_required
def editcategory():
    """ A form that edits the category """
    currentuser = provide_user()
    return render_template('editcategory.html',
                           title='editcategory',
                           user=currentuser)


@APP.route('/editrecipe', methods=['GET', 'POST'])
@login_required
def editrecipe():
    """ Here you can edit the details of the recipe """
    currentuser = provide_user()
    return render_template('editrecipe.html',
                           title='editrecipe',
                           user=currentuser)


@APP.route('/profile', methods=['GET'])
@login_required
def profile():
    """ Here the use r can view his/her profile """
    currentuser = provide_user()
    return render_template('profile.html',
                           title='profile',
                           user=currentuser)


@APP.route('/recipe', methods=['GET'])
@login_required
def recipe():
    """ This is where you view the recipe"""
    currentuser = provide_user()
    return render_template('recipe.html',
                           title='recipe',
                           user=currentuser)


@APP.route('/signin', methods=['GET', 'POST'])
def signin():
    """ This is the page where you sign in """
    form = LoginForm(request.form)
    error = None
    if request.method == 'POST' and form.validate():
        for user in users:
            if user.email == form.email.data and\
                    user.password == form.password.data:
                session['logged_in'] = user.email
                return redirect('/profile')
            else:
                flash("Your email or password is wrong")
    return render_template('signin.html',
                           title='signin',
                           form=form)


@APP.route('/signup', methods=['GET', 'POST'])
def signup():
    """ This is a form that takes sign up details """
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        user = User(form.username.data,
                    form.email.data,
                    form.bio.data,
                    form.password.data
                    )
        users.append(user)
        return redirect('/profile')
    return render_template('signup.html',
                           title='signup',
                           form=form)


@APP.route('/viewcategory')
@login_required
def viewcategory():
    """ You can view the list of categories """
    currentuser = provide_user()
    return render_template('viewcategory.html',
                           title='viewcategory',
                           user=currentuser)


@APP.route('/viewrecipe')
@login_required
def viewrecipe():
    """ You can see a list of recipes """
    currentuser = provide_user()
    return render_template('viewrecipe.html',
                           title='viewrecipe',
                           user=currentuser)


@APP.route('/logout')
@login_required
def logout():
    """ remove the session if it's there """
    session.clear()
    return redirect(url_for('index'))
