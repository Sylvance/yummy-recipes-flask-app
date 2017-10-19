""" Views file for the flask app"""
from flask import render_template, flash, redirect
from app import app
from .forms import (SigninForm,
                    SignupForm,
                    AddcategoryForm,
                    AddrecipeForm,
                    EditcategoryForm,
                    EditrecipeForm)


@app.route('/')
@app.route('/index')
def index():
    """ Place a Docstring here """
    user = {'nickname': 'Sylvance', 'job': 'Carpernter',
            'categoriesno': 8, 'recipesno': 23}
    return render_template('home.html',
                           title='Home',
                           user=user)


@app.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    """ Place a Docstring here """
    user = {'nickname': 'Sylvance', 'job': 'Carpernter',
            'categoriesno': 8, 'recipesno': 23}
    form = AddcategoryForm()
    if form.validate_on_submit():

        return redirect('/profile')
    return render_template('addcategory.html',
                           title='addcategory',
                           user=user,
                           form=form)


@app.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
    """ Place a Docstring here """
    user = {'nickname': 'Sylvance', 'job': 'Carpernter',
            'categoriesno': 8, 'recipesno': 23}
    form = AddrecipeForm()
    if form.validate_on_submit():

        return redirect('/profile')
    return render_template('addrecipe.html',
                           title='addrecipe',
                           user=user,
                           form=form)


@app.route('/category')
def category():
    """ Place a Docstring here """
    user = {'nickname': 'Sylvance', 'job': 'Carpernter',
            'categoriesno': 8, 'recipesno': 23}
    return render_template('category.html',
                           title='category',
                           user=user)


@app.route('/editcategory', methods=['GET', 'POST'])
def editcategory():
    """ Place a Docstring here """
    user = {'nickname': 'Sylvance', 'job': 'Carpernter',
            'categoriesno': 8, 'recipesno': 23}
    form = EditcategoryForm()
    if form.validate_on_submit():

        return redirect('/profile')
    return render_template('editcategory.html',
                           title='editcategory',
                           user=user,
                           form=form)


@app.route('/editrecipe', methods=['GET', 'POST'])
def editrecipe():
    """ Place a Docstring here """
    user = {'nickname': 'Sylvance', 'job': 'Carpernter',
            'categoriesno': 8, 'recipesno': 23}
    form = EditrecipeForm()
    if form.validate_on_submit():

        return redirect('/profile')
    return render_template('editrecipe.html',
                           title='editrecipe',
                           user=user,
                           form=form)


@app.route('/profile')
def profile():
    """ Place a Docstring here """
    user = {'nickname': 'Sylvance', 'job': 'Carpernter',
            'categoriesno': 8, 'recipesno': 23}
    return render_template('profile.html',
                           title='profile',
                           user=user)


@app.route('/recipe')
def recipe():
    """ Place a Docstring here """
    user = {'nickname': 'Sylvance', 'job': 'Carpernter',
            'categoriesno': 8, 'recipesno': 23}
    return render_template('recipe.html',
                           title='recipe',
                           user=user)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """ Place a Docstring here """
    form = SigninForm()
    if form.validate_on_submit():

        flash('Signin requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/profile')
    return render_template('signin.html',
                           title='signin',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ Place a Docstring here """
    form = SignupForm()
    if form.validate_on_submit():

        return redirect('/profile')
    return render_template('signup.html',
                           title='signup',
                           form=form)


@app.route('/viewcategory')
def viewcategory():
    """ Place a Docstring here """
    user = {'nickname': 'Sylvance', 'job': 'Carpernter',
            'categoriesno': 8, 'recipesno': 23}
    return render_template('viewcategory.html',
                           title='viewcategory',
                           user=user)


@app.route('/viewrecipe')
def viewrecipe():
    """ Place a Docstring here """
    user = {'nickname': 'Sylvance', 'job': 'Carpernter',
            'categoriesno': 8, 'recipesno': 23}
    return render_template('viewrecipe.html',
                           title='viewrecipe',
                           user=user)

if __name__ == '__main__':
    app.run(debug=True,
            host="0.0.0.0",
            port="8888")
