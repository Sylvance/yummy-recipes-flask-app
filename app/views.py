from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def index():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('home.html',
                           title='Home',
                           user=user)
@app.route('/addcategory')
def addcategory():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('addcategory.html',
                           title='addcategory',
                           user=user)

@app.route('/addrecipe')
def addrecipe():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('addrecipe.html',
                           title='addrecipe',
                           user=user)

@app.route('/category')
def category():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('category.html',
                           title='category',
                           user=user)

@app.route('/editcategory')
def editcategory():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('editcategory.html',
                           title='editcategory',
                           user=user)

@app.route('/editrecipe')
def editrecipe():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('editrecipe.html',
                           title='editrecipe',
                           user=user)

@app.route('/profile')
def profile():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('profile.html',
                           title='profile',
                           user=user)

@app.route('/recipe')
def recipe():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('recipe.html',
                           title='recipe',
                           user=user)

@app.route('/signin')
def signin():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('signin.html',
                           title='signin',
                           user=user)

@app.route('/signup')
def signup():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('signup.html',
                           title='signup',
                           user=user)

@app.route('/viewcategory')
def viewcategory():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('viewcategory.html',
                           title='viewcategory',
                           user=user)

@app.route('/viewrecipe')
def viewrecipe():
    user = {'nickname': 'Sylvance', 'job' : 'Carpernter', 'categoriesno' : 8, 'recipesno' : 23}  
    return render_template('viewrecipe.html',
                           title='viewrecipe',
                           user=user)