#!/usr/bin/python3
""" Module City for HBNB project """

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
<<<<<<< HEAD
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', cascade='all, delete', backref='cities')
=======
    """Representation of city """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="delete")

    else:
        state_id = ""
        name = ""

        def __init__(self, *args, **kwargs):
            """intializes city"""
            super().__init__(*args, **kwargs)
>>>>>>> bda0defce45be6a56ad9a352c82c748b52567ed2
