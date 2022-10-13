#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel, Column, String
from models import storage_type

class Amenity(BaseModel, Base):
    """class model for amenity in a place"""
    if storage_type == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
