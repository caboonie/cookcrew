from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///recipes.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_recipe(name,servings,ingredients,recipe):
    recipe_object = Recipe(name=name,servings=servings,ingredients=ingredients,recipe=recipe)
    session.add(recipe_object)
    session.commit()

def get_all_recipes():
    recipes = session.query(Recipe).all()
    return recipes

def get_recipe(id):
    recipe = session.query(Recipe).filter_by(id=id).first()
    return recipe

