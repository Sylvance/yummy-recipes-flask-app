""" Class for recipes """
from uuid import uuid4

class Recipe(object):
    """ Recipe class """

    def __init__(self, recipetitle, recipedescription):
        """ Construct recipe"""
        self.id = uuid4().hex
        self.recipetitle = recipetitle
        self.recipedescription = recipedescription

    def __repr__(self):
        return '{}'.format(self.recipetitle)