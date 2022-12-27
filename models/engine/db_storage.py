#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

classes = {'User': User, 'State': State, 'Review': Review,
           'Place': Place, 'City': City, 'Amenity': Amenity}


class DBStorage:
    """A class for database storage"""
    __session = None
    __engine = None

    def __init__(self):
        """initializes instances"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                           pool_pre_ping=True)
        if HBNB_ENV == 'test' or HBNB_ENV == 'dev':
            Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary of all objects present in a class or every class if cls=None"""
        new_dic = {}
        if cls is None:
            for val in classes.values():
                objects = self.__session.query(val).all()
                for i in objects:
                    key = i.__class__.__name__ + '.' + i.id
                    new_dic[key] = i
        else:
            objects = self.__session.query(cls).all()
            for i in objects:
                key = i.__class__.__name__ + '.' + i.id
                new_dic[key] = i
        return new_dic

    def new(self, obj):
        """Adds a new instance to the database"""
        if obj is not None:
            self.__session.add(obj)
            

    def save(self):
        """saves the new object instance to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object instance from the database"""
        if obj is not None:
            self.__session.query(obj).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """refreshes the database"""
        Base.metadata.create_all(self.__engine)
        sessionfresh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sessionfresh)
