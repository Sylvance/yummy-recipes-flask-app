""" Views file for the flask app"""
from flask import render_template, session, redirect, url_for, request
# from werkzeug.utils import secure_filename
from app import app

DATABASE = [
    ("User1", "password"),
    ("User2", "password")
]

USER = {'nickname': 'Sylvance', 'job': 'Carpernter', 'categoriesno': 8, 'recipesno': 23}

@app.route('/')
@app.route('/index')
def index():
    """ Place a Docstring here """
    return render_template('home.html',
                           title='Home')


@app.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    """ Place a Docstring here """
    return render_template('addcategory.html',
                           title='addcategory',
                           user=USER)


@app.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
    """ Place a Docstring here """
    return render_template('addrecipe.html',
                           title='addrecipe',
                           user=USER)


@app.route('/category')
def category():
    """ Place a Docstring here """
    return render_template('category.html',
                           title='category',
                           user=USER)


@app.route('/editcategory', methods=['GET', 'POST'])
def editcategory():
    """ Place a Docstring here """
    return render_template('editcategory.html',
                           title='editcategory',
                           user=USER)


@app.route('/editrecipe', methods=['GET', 'POST'])
def editrecipe():
    """ Place a Docstring here """
    return render_template('editrecipe.html',
                           title='editrecipe',
                           user=USER)


@app.route('/profile')
def profile():
    """ Place a Docstring here """
    return render_template('profile.html',
                           title='profile',
                           user=USER)


@app.route('/recipe')
def recipe():
    """ Place a Docstring here """
    return render_template('recipe.html',
                           title='recipe',
                           user=USER)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """ Place a Docstring here """
    if request.method == 'POST':

        session['username'] = request.form['username']
        username = request.form['username']
        password = request.form['password']
        if (username, password) in DATABASE:
            return redirect('/profile')
        return redirect('/signin')

    return render_template('signin.html',
                           title='signin')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ Place a Docstring here """
    if request.method == 'POST':
        session['username'] = request.form['username']
        newusername = request.form['username']
        newpassword = request.form['password']
        DATABASE.append((newusername, newpassword))
        return redirect('/profile')
    return render_template('signup.html',
                           title='signup')


@app.route('/viewcategory')
def viewcategory():
    """ Place a Docstring here """
    return render_template('viewcategory.html',
                           title='viewcategory',
                           user=USER)


@app.route('/viewrecipe')
def viewrecipe():
    """ Place a Docstring here """
    return render_template('viewrecipe.html',
                           title='viewrecipe',
                           user=USER)


@app.route('/logout')
def logout():
    """ remove the username from the session if it's there """
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True,
            host="0.0.0.0",
            port="8888")
