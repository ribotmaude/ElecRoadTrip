# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 08:29:43 2021

@author: raffelet
"""

# flask_sqlalchemy/models.py
import sqlalchemy as sqa
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

sqa.engine = sqa.create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=sqa.engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Voiture(Base):
    __tablename__ = 'voiture'
    id = sqa.Column(sqa.Integer, primary_key=True)
    name = sqa.Column(sqa.String)
    marque = sqa.Column(sqa.String)
    autonomie = sqa.Column(sqa.Integer)
    temps_chargement = sqa.Column(sqa.Integer)
    

