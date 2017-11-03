""" The tests for the app"""
import unittest
import flask

from app import APP
from app.models.recipe import Recipe
from app.models.category import Category
from app.models.users import User


class BasicTestCase(unittest.TestCase):
    """
    These are tests for the url enpoints for the app.
       The url endpoints are;
          1. / (get)
          2. /index (get)
          3. /addcategory (get, post)
          4. /addrecipe/<categoryid> (get, post)
          5. /category/<categoryid> (get)
          6. /editcategory/<id> (get, post)
          7. /editrecipe/<categoryid>/<recipeid> (get, post)
          8. /viewcategory (get)
          9. /viewrecipe (get)
          10. /deletecategory/<id> (get)
          11. /deleterecipe/<categoryid>/<recipeid> (get)
          12. /profile (get)
          13. /recipe/<categoryid>/<recipeid> (get)
          14. /signin (get, post)
          15. /signup (get, post)
          16. /logout
    """

    def setUp(self):
        """
        Sets up tests Category object : 
            Category(categorytitle, categorydescription)

        The constructor of the Category class is; 
            self.categorytitle = categorytitle
            self.categorydescription = categorydescription
        """
        self.new_user = User('sylvance', 'sylvance@mail',
                             'I am good', 'Scifi4u*@')
        self.categoryid = self.new_user.create_category('Chinese dishes',
                                                        'Dishes made in China')
        self.sample_category = Category('Kenyan dishes',
                                        'Dishes made in Kenya')
        self.recipeid = self.sample_category.add_recipe('not chapati',
                                                        'not round or brown or good')
        APP.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    def test_index(self):
        """ 
            A test for loading of the landing page
            The url endpoint is;
                =>    / (get)
        """
        tester = APP.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        """ 
            A test for loading of the home page
            The url endpoint is;
                =>    /index (get)
        """
        tester = APP.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_addcategory(self):
        """ 
            A test for loading of the addcategory page
            The url endpoint is;
                =>    /addcategory (get, post)
        """
        tester = APP.test_client(self)
        response = tester.get('/addcategory', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_addrecipe(self):
        """ 
            A test for loading of the addrecipe page
            The url endpoint is;
                =>    /addrecipe/<categoryid> (get, post)
        """
        with APP.test_request_context('/addrecipe/?categoryid=Kenyan'):
            assert flask.request.path == '/addrecipe/'
            assert flask.request.args['categoryid'] == 'Kenyan'

    def test_category(self):
        """ 
            A test for loading of the category page
            The url endpoint is;
                =>    /category/<categoryid> (get)
        """
        tester = APP.test_client(self)
        response = tester.get('/category', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_editcategory(self):
        """ 
            A test for loading of the editcategory page
            The url endpoint is;
                =>    /editcategory/<id> (get, post)
        """
        with APP.test_request_context('/editcategory/?categoryid=Kenyan'):
            assert flask.request.path == '/editcategory/'
            assert flask.request.args['categoryid'] == 'Kenyan'

    def test_editrecipe(self):
        """ 
            A test for loading of the editrecipe page
            The url endpoint is;
                =>    /editrecipe/<categoryid>/<recipeid> (get, post)
        """
        with APP.test_request_context('/editrecipe/?categoryid=Kenyan/?recipeid=Chapati'):
            assert flask.request.path == '/editrecipe/'
            assert flask.request.args['categoryid'] == 'Kenyan'
            assert flask.request.args['categoryid'] == 'Kenyan'

    def test_profile(self):
        """ 
            A test for loading of the editrecipe page
            The url endpoint is;
                =>    /profile (get)
        """
        tester = APP.test_client(self)
        response = tester.get('/profile', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_recipe(self):
        """ 
            A test for loading of the editrecipe page
            The url endpoint is;
                =>    /recipe/<categoryid>/<recipeid> (get)
        """
        tester = APP.test_client(self)
        response = tester.get('/recipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signin(self):
        """ 
            A test for loading of the sigin page
            The url endpoint is;
                =>    /signin (get)
        """
        tester = APP.test_client(self)
        response = tester.get('/signin', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        """ 
            A test for loading of the signup page
            The url endpoint is;
                =>    /signup (get, post)
        """
        tester = APP.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_logout(self):
        """ 
            A test for loading of the editrecipe page
            The url endpoint is;
                =>    /logout (get)
        """
        r = APP.test_client(self)
        return r.get('/logout', follow_redirects=True)

    def test_viewcategory(self):
        """ 
            A test for loading of the editrecipe page
            The url endpoint is;
                =>    /viewcategory (get)
        """
        tester = APP.test_client(self)
        response = tester.get('/viewcategory', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_viewrecipe(self):
        """ 
            A test for loading of the editrecipe page
            The url endpoint is;
                =>    /viewrecipe (get)
        """
        tester = APP.test_client(self)
        response = tester.get('/viewrecipe', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class TestCategory(unittest.TestCase):
    """
    These are tests for Category methods.
       The Category methods are;
          1. Add recipe
          2. Edit recipe
          3. Delete recipe 
    """

    def setUp(self):
        """
        Sets up tests Category object : 
            Category(categorytitle, categorydescription)

        The constructor of the Category class is; 
            self.categorytitle = categorytitle
            self.categorydescription = categorydescription
        """
        self.sample_category = Category('Kenyan dishes',
                                        'Dishes made in Kenya')

    def test_add_recipe(self):
        """ Test whether a recipe has been saved """
        before_add = len(self.sample_category.recipes)
        self.sample_category.add_recipe('chapati',
                                        'round brown and good')
        after_add = len(self.sample_category.recipes)
        self.assertEqual(after_add - before_add, 1)

    def test_edit_recipe(self):
        """ Test whether  an recipe has been edited """
        id = self.sample_category.add_recipe('not chapati',
                                             'not round or brown or good')
        self.sample_category.edit_recipe(id,
                                         'chapati',
                                         'round brown and good')
        recipe = self.sample_category.recipes[id]
        self.assertEqual(
            recipe.recipetitle,
            'chapati')

    def test_delete_recipe(self):
        """Test whether a recipe has been deleted"""
        id = self.sample_category.add_recipe('not chapati',
                                             'not round or brown or good')
        size_before = len(self.sample_category.recipes)
        self.sample_category.delete_recipe(id)
        size_after = len(self.sample_category.recipes)
        self.assertTrue(size_before - size_after, 1)


class TestUser(unittest.TestCase):
    """
    These are tests for User methods.
       The User methods are (what a user is able to do);
          1. Add category
          2. Edit category
          3. Delete category 
    """

    def setUp(self):
        """
        Sets up tests User object : 
            User(username, email, bio, password)

        The constructor of the Category class is; 
            self.username = username
            self.email = email
            self.bio = bio
            self.password = password
        """
        self.new_user = User('sylvance', 'sylvance@mail',
                             'I am good', 'Scifi4u*@')

    def test_create_category(self):
        """ Test whether category has been  created """
        result = len(self.new_user.categories)
        self.new_user.create_category('Kenyan dishes',
                                      'Dishes made in Kenya')
        after_add = len(self.new_user.categories)
        self.assertEqual(after_add - result, 1)

    def test_update_category(self):
        """ Test whether category has been edited"""
        id = self.new_user.create_category('Chinese dishes',
                                           'Dishes made in China')
        self.new_user.update_category(id,
                                      'Chinese dishes reloaded',
                                      'Made in China')
        category = self.new_user.categories[id]
        self.assertEqual(category.categorytitle,
                         'Chinese dishes reloaded'
                         )
        self.assertEqual(category.categorydescription,
                         'Made in China')

    def test_delete_category(self):
        """ Test whether  category has been deleted """
        id = self.new_user.create_category('Indian dishes',
                                           'Dishes made in India')
        result = len(self.new_user.categories)
        self.new_user.delete_category(id)
        after_delete = len(self.new_user.categories)
        self.assertTrue(result, after_delete)

if __name__ == '__main__':
    unittest.main()
