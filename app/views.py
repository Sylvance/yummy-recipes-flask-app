""" Views file for the Flask APP"""
from flask import render_template, session, redirect, url_for, flash, request
from wtforms import Form, StringField, SelectField, PasswordField, \
    TextField, TextAreaField, validators
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
    categorytitle = StringField('categorytitle', [validators.DataRequired()])
    categorydescription = StringField(
        'description', [validators.DataRequired()])


class CreateRecipe(Form):
    """creates form input field for adding recipe"""
    recipetitle = StringField('recipetitle', [validators.DataRequired()])
    recipedescription = TextAreaField('recipedescription')


class EditRecipe(Form):
    """creates form input field for editing recipe"""
    recipetitle = StringField('recipetitle', [validators.DataRequired()])
    recipedescription = StringField(
        'recipedescription', [validators.DataRequired()])


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
                flash(u'You just created a new category! Woo Hoo!')
                return redirect('/viewcategory')
            else:
                flash("You should login first")
    return render_template('addcategory.html',
                           title='addcategory',
                           form=form,
                           user=currentuser)


@APP.route('/addrecipe/<categoryid>', methods=['GET', 'POST'])
@login_required
def addrecipe(categoryid):
    """ A form that adds a new recipe """
    form = CreateRecipe(request.form)
    currentuser = provide_user()
    error = None
    if request.method == 'POST' and form.validate():
        for user in users:
            if user.email == session['logged_in']:
                for category in user.categories.values():
                    if categoryid == category.id:
                        category.add_recipe(
                            form.recipetitle.data, form.recipedescription.data)
                        flash(u'You just made a new recipe.')
                        return redirect(url_for('viewrecipe'))
    return render_template('addrecipe.html',
                           title='addrecipe',
                           form=form,
                           categoryid=categoryid,
                           user=currentuser)


@APP.route('/category/<categoryid>', methods=['GET'])
@login_required
def category(categoryid):
    """ This is a view page for the category """
    currentuser = provide_user()
    for user in users:
        if user.email == session['logged_in']:
            category = user.categories[categoryid]
            recipes = user.categories[categoryid].recipes
            return render_template('category.html',
                                   title='category',
                                   category=category,
                                   recipes=recipes,
                                   user=currentuser)


@APP.route('/editcategory/<id>', methods=['GET', 'POST'])
@login_required
def editcategory(id):
    """ A form that edits the category """
    form = EditCategory(request.form)
    currentuser = provide_user()
    error = None
    if request.method == 'POST' and form.validate():
        for user in users:
            if user.email == session['logged_in']:
                user.update_category(id,
                                     form.categorytitle.data,
                                     form.categorydescription.data)
                flash(u'Your category is updated.')
                return redirect('/viewcategory')
    return render_template('editcategory.html',
                           title='editcategory',
                           categoryid=id,
                           form=form,
                           user=currentuser)


@APP.route('/editrecipe/<categoryid>/<recipeid>', methods=['GET', 'POST'])
@login_required
def editrecipe(categoryid, recipeid):
    """ Here you can edit the details of the recipe """
    form = EditRecipe(request.form)
    currentuser = provide_user()
    error = None
    if request.method == 'POST' and form.validate():
        for user in users:
            if user.email == session['logged_in']:
                recipetitle = form.recipetitle.data
                recipedescription = form.recipedescription.data
                user.categories[categoryid].edit_recipe(recipeid,
                                                        recipetitle,
                                                        recipedescription)
                flash(u'Your recipe is updated.')
                return redirect('/viewrecipe')
    return render_template('editrecipe.html',
                           title='editrecipe',
                           form=form,
                           user=currentuser)


@APP.route('/viewcategory')
@login_required
def viewcategory():
    """ You can view the list of categories """
    currentuser = provide_user()
    for user in users:
        if user.email == session['logged_in']:
            categories = user.categories
            return render_template('viewcategory.html',
                                   title='viewcategory',
                                   categories=categories,
                                   user=currentuser)


@APP.route('/viewrecipe')
@login_required
def viewrecipe():
    """ You can see a list of recipes """
    currentuser = provide_user()
    for user in users:
        if user.email == session['logged_in']:
            categories = user.categories
    return render_template('viewrecipe.html',
                           title='viewrecipe',
                           categories=categories,
                           user=currentuser)


@APP.route('/deletecategory/<id>', methods=['GET'])
@login_required
def deletecategory(id):
    """ A form that edits the category """
    for user in users:
        if user.email == session['logged_in']:
            user.delete_category(id)
            flash(u'You just deleted a category')
            return redirect('/viewcategory')


@APP.route('/deleterecipe/<categoryid>/<recipeid>', methods=['GET'])
@login_required
def deleterecipe(categoryid, recipeid):
    """ Here you can edit the details of the recipe """
    for user in users:
        if user.email == session['logged_in']:
            user.categories[categoryid].delete_recipe(recipeid)
            flash(u'You just deleted a recipe.')
            return redirect('/viewrecipe')


@APP.route('/profile', methods=['GET'])
@login_required
def profile():
    """ Here the use r can view his/her profile """
    currentuser = provide_user()
    for user in users:
        if user.email == session['logged_in']:
            categories = user.categories
            return render_template('profile.html',
                                   title='profile',
                                   categories=categories,
                                   user=currentuser)
    return redirect('/index')


@APP.route('/recipe/<categoryid>/<recipeid>', methods=['GET'])
@login_required
def recipe(categoryid, recipeid):
    """ This is where you view the recipe"""
    currentuser = provide_user()
    for user in users:
        if user.email == session['logged_in']:
            recipe = user.categories[categoryid].recipes[recipeid]
            return render_template('recipe.html',
                                   title='recipe',
                                   recipe=recipe,
                                   categoryid=categoryid,
                                   user=currentuser)
    return redirect('/index')


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
                flash(u'Welcome back.')
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
        flash('Thanks for registering')
        return redirect(url_for('profile'))
    return render_template('signup.html',
                           title='signup',
                           form=form)


@APP.route('/logout')
@login_required
def logout():
    """ remove the session if it's there """
    session.clear()
    flash(u'Bye. Welcome back again!')
    return redirect(url_for('index'))
