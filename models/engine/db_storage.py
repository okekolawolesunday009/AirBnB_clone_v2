#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    def __init__(self):
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                    getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self._engine)

    def all(self, cls=None):
        '''Run a query on the Current database session'''
        all_dict = {}
        self.close()
        if cls:
            for item in self.__session.query(cls).all():
                key = '{}.{}'.format(item.__class__.name, item.id)
                all_dict[key] = item
        else:
            for item, value in self.classes.items():
                if type(value) is not type(BaseModel):
                    for it in self.__session.query(value).all():
                        key = '{}.{}'.format(it.__class__.__name__, it.id)
                        all_dict[key] = it
        return all_dict

    def new(self, obj):
        """add new obj"""
        try:
            if obj not in self.__session:
                self.__session.add(obj)
            else:
                self.__session.close()
        except Exception as e:
            print(f"Error session on database: {e}")
            raise

    def save(self):
        """save new obj"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete new obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload new obj"""
        try:
            Base.metadata.create_all(self.__engine)
            Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
            with Session() as session:
                self.__session = session
        except Exception as e:
            print(f"Error reloading database: {e}")
            raise

    def close(self):
        """close new obj session"""
        self.__session.close()
