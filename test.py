""" The tests for the app"""
import unittest

from app import APP


class BasicTestCase(unittest.TestCase):
    """ The Basic Test cases for this APP"""

    def test_index(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_addcategory(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/addcategory', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_addrecipe(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/addrecipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_category(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/category', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_editcategory(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/editcategory', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_editrecipe(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/editrecipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/profile', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_recipe(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/recipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signin(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/signin', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_viewcategory(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/viewcategory', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_viewrecipe(self):
        """ A test"""
        tester = APP.test_client(self)
        response = tester.get('/viewrecipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
