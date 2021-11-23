# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:10:02 2021

@author: Mbrt_
"""

# =============================================================================
# IMPORT
# =============================================================================

from zeep import Client


class Soap_manager():

# =============================================================================
# CONSTRUCTEUR
# =============================================================================
    def __init__(self):
        #Création du client Soap
        self.client = Client('http://127.0.0.1:8000/?wsdl')
        
# =============================================================================
# FONCTIONS
# =============================================================================
    def get_soap_distance(self, total_distance, nbr_stop, temps_chargement):
        
        #Appel de la fonction Soap pour calculer le temps de trajet
        trip_time = self.client.service.get_temps_trajet(total_distance, nbr_stop, temps_chargement)
        
        return trip_time
    
# =============================================================================
# MAIN
# =============================================================================

# soap_manager = Soap_manager()
# test = soap_manager.get_soap_distance(100,3,30)
# print(test)

