""" Views file for the Flask APP"""
from flask import render_template, session, redirect, url_for, request
# from werkzeug.utils import secure_filename
from app import APP

USERS = []
PASSWORDS = []
CATEGORIES = []
RECIPES = []

DATABASE = {}


class User(object):
    """ Users class """

    def __init__(self):
        self.id = ''
        self.password = ''
        self.bio = ''
        self.categories = []
        self.recipes = []

    def add_dbuser(username, bio, password):
        USERS.append(username)
        DATABASE[user]['password'] = password
        DATABASE[user]['bio'] = bio
        DATABASE[user]['categories'] = []
        DATABASE[user]['recipes'] = []

    def edit_dbuserpassword(username, password):
        DATABASE[user]['password'] = password

    def edit_dbuserbio(username, bio):
        DATABASE[user]['bio'] = bio

    def view_dbuser(user):
        DATABASE[user]

    def delete_dbuser(user, recipeid):
        del DATABASE[user]


class Categories(object):
    """ Categories class """

    def __init__(self):
        self.owner = ''
        self.categoryname = ''
        self.categorydescription = ''

    def add_dbcategory(owner, 
                      categoryname, 
                      categorydescription):
        if owner in list(DATABASE.keys()):
            category = {
                'owner': owner,
                'categoryname': categoryname,
                'categorydescription': categorydescription
            }
            CATEGORIES.append(categoryname)
            DATABASE[owner]['categories'].append(category)

    def edit_dbcategory(owner, 
                        categoryname, 
                        categorydescription):
        if owner in list(DATABASE.keys()):
            category = {
                'owner': owner,
                'categoryname': categoryname,
                'categorydescription': categorydescription
            }
            CATEGORIES.append(categoryname)
            DATABASE[owner]['categories'].append(category)

    def view_dbusercategories(user):
        DATABASE[user]['categories']

    def view_dbcategory(user, categoryid):
        DATABASE[user]['categories'][categoryid]

    def del_dbcategory(user, categoryid):
      del DATABASE[user]['categories'][categoryid]


class Recipes(object):
    """ Recipes class """

    def __init__(self):
        self.owner = ''
        self.recipename = ''
        self.recipedescription = ''
        self.recipeingredients = ''
        self.recipecategory = ''

    def add_dbrecipe(owner, 
                     recipename, 
                     recipedescription, 
                     recipeingredients, 
                     recipecategory):
        if owner in list(DATABASE.keys()):
            RECIPES.append(recipename)
            recipeid = RECIPES[-1]
            recipe = {
                'owner': owner,
                'recipeid': recipeid,
                'recipename': recipename,
                'recipeingredients': recipeingredients,
                'recipedescription': recipedescription,
                'recipecategory': recipecategory
            }
            DATABASE[owner]['recipes'].append(recipe)

    def view_dbuserrecipes(user):
        DATABASE[user]['recipes']

    def view_dbrecipe(user, recipeid):
        DATABASE[user]['recipes'][recipeid]

    def delete_dbrecipe(user, recipeid):
      del DATABASE[user]['recipes'][recipeid]


@APP.route('/')
@APP.route('/index')
def index():
    """ Here the user sees the signup and signin gateways """
    return render_template('home.html',
                           title='Home')


@APP.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    """ A form to add a new category """
    return render_template('addcategory.html',
                           title='addcategory',
                           user=session['username'])


@APP.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
    """ A form that adds a new recipe """
    # if request.method == 'POST':
    #     session['username']
    #     recipename = request.form['recipename']
    #     recipeingredients = request.form['recipeingredients']
    #     recipedescription = request.form['recipedescription']
    #     recipecategory = request.form['recipecategory']
    #     return redirect('/profile')
    return render_template('addrecipe.html',
                           title='addrecipe',
                           user=session['username'])


@APP.route('/category')
def category():
    """ This is a view page for the category """
    return render_template('category.html',
                           title='category',
                           user=session['username'])


@APP.route('/editcategory', methods=['GET', 'POST'])
def editcategory():
    """ A form that edits the category """
    return render_template('editcategory.html',
                           title='editcategory',
                           user=session['username'])


@APP.route('/editrecipe', methods=['GET', 'POST'])
def editrecipe():
    """ Here you can edit the details of the recipe """
    return render_template('editrecipe.html',
                           title='editrecipe',
                           user=session['username'])


@APP.route('/profile')
def profile():
    """ Here the use r can view his/her profile """
    return render_template('profile.html',
                           title='profile',
                           user=session['username'])


@APP.route('/recipe')
def recipe():
    """ This is where you view the recipe"""
    return render_template('recipe.html',
                           title='recipe',
                           user=session['username'])


@APP.route('/signin', methods=['GET', 'POST'])
def signin():
    """ This is the page where you sign in """
    if request.method == 'POST':

        session['username'] = request.form['username']
        username = request.form['username']
        password = request.form['password']
        # if (username, password) in DATABASE:
        return redirect('/profile')
        # return redirect('/signin')

    return render_template('signin.html',
                           title='signin')


@APP.route('/signup', methods=['GET', 'POST'])
def signup():
    """ This is a form that takes sign up details """
    if request.method == 'POST':
        session['username'] = request.form['username']
        newusername = request.form['username']
        newpassword = request.form['password']
        return redirect('/profile')
    return render_template('signup.html',
                           title='signup')


@APP.route('/viewcategory')
def viewcategory():
    """ You can view the list of categories """
    return render_template('viewcategory.html',
                           title='viewcategory',
                           user=session['username'])


@APP.route('/viewrecipe')
def viewrecipe():
    """ You can see a list of recipes """
    return render_template('viewrecipe.html',
                           title='viewrecipe',
                           user=session['username'])


@APP.route('/logout')
def logout():
    """ remove the username from the session if it's there """
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
APP.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    APP.run(debug=True,
            host="0.0.0.0",
            port="8888")
