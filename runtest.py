from app import app

import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_addcategory(self):
        tester = app.test_client(self)
        response = tester.get('/addcategory', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_addrecipe(self):
        tester = app.test_client(self)
        response = tester.get('/addrecipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_category(self):
        tester = app.test_client(self)
        response = tester.get('/category', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_editcategory(self):
        tester = app.test_client(self)
        response = tester.get('/editcategory', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_editrecipe(self):
        tester = app.test_client(self)
        response = tester.get('/editrecipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        tester = app.test_client(self)
        response = tester.get('/profile', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/recipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signin(self):
        tester = app.test_client(self)
        response = tester.get('/signin', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_viewcategory(self):
        tester = app.test_client(self)
        response = tester.get('/viewcategory', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_viewrecipe(self):
        tester = app.test_client(self)
        response = tester.get('/viewrecipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()