#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import Base, BaseModel, Column, String
from models import storage_type
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename = 'states'
        name = Column(String(128))
        cities = relationship('City', backref='states')
    else:
        @property
        def cities(self):
            from models import storage
            cities = storage.all(City)
            instances = []
            for city in cities.values():
                if city.id == self.id:
                    instances.append(city)
            return instances

