""" Model for category class """
from uuid import uuid4
from .recipe import Recipe


class Category(object):
    """Category class"""

    def __init__(self, categorytitle, categorydescription):
        """Category object constructor"""
        self.categorytitle = categorytitle
        self.categorydescription = categorydescription
        self.id = uuid4().hex

        self.recipes = dict()

    def add_recipe(self, recipetitle, recipedescription):
        """ Creates and add recipe to dictionary"""
        new_recipe = Recipe(recipetitle, recipedescription)
        self.recipes[new_recipe.id] = new_recipe
        return new_recipe.id

    def edit_recipe(self, id, recipetitle, recipedescription):
        """ Edit existing recipe"""
        for key in self.recipes.copy().keys():
            if id == key:
                self.recipes[key].recipetitle = recipetitle
                self.recipes[key].recipedescription = recipedescription

    def delete_recipe(self, id):
        """ Delete a recipe"""
        for key in self.recipes.copy().keys():
            if id == key:
                del self.recipes[key]

    def __repr__(self):
        return '{}'.format(self.categorytitle)
