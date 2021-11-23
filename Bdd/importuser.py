# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:03:24 2021

@author: mribot
"""
import models as mod
mod.Base.metadata.create_all(bind=mod.sqa.engine)

# Fill the tables with some data
Fiesta = mod.Voiture(name='Fiesta',marque='Ford',autonomie=130,temps_chargement=23)
mod.db_session.add(Fiesta)

Clio = mod.Voiture(name='Clio',marque='Renault',autonomie=140,temps_chargement=30)
mod.db_session.add(Clio)

Mustang = mod.Voiture(name='Mustang',marque='Ford',autonomie=180,temps_chargement=38)
mod.db_session.add(Mustang)

mod.db_session.commit()