from sqlalchemy import Column, Integer, String, Boolean,PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    servings = Column(Integer)
    ingredients = Column(PickleType)
    recipe = Column(String)
