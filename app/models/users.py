""" Model for the User class """

from .category import Category

class User(object):
    """ User class"""

    def __init__(self, username, email, bio, password):
        """ Construct the user """
        self.username = username
        self.email = email
        self.bio = bio
        self.password = password

        self.categories = dict()

    def create_category(self, categorytitle, categorydescription):
        """ Add a new category"""
        new_category = Category(categorytitle, categorydescription)
        self.categories[new_category.id] = new_category
        return new_category.id

    def update_category(self, id, categorytitle, categorydescription):
        """ Updating existing categories """
        for key in self.categories.copy().keys():
            if id == key:
                self.categories[key].categorytitle = categorytitle
                self.categories[key].categorydescription = categorydescription


    def delete_category(self, id):
        """ Delete category """
        for key  in self.categories.copy().keys():
            if id == key:
                del self.categories[key]

    def __repr__(self):
        return '{}'.format(self.username)