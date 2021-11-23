# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 08:33:28 2021

@author: raffelet
"""

# flask_sqlalchemy/schema.py
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Voiture as VoitureModel


class Voiture(SQLAlchemyObjectType):
    class Meta:
        model = VoitureModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_voitures = SQLAlchemyConnectionField(Voiture.connection)

schema = graphene.Schema(query=Query)