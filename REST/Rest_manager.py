# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:05:10 2021

@author: Mbrt_
"""

# =============================================================================
# IMPORT
# =============================================================================
from Server_Rest import Server_Rest 


class Rest_manager():

# =============================================================================
# CONSTRUCTEUR
# =============================================================================
    def __init__(self):
        self.server_rest = Server_Rest()
        
# =============================================================================
# FONCTIONS
# =============================================================================
    def get_bornes_address(self, depart_add, arriv_add, autonomie):
        
        #récupération des coordonnées des adresses de départ et d'arrivée
        coord_d_add = self.server_rest.get_coordinates(depart_add)
        coord_a_add = self.server_rest.get_coordinates(arriv_add)
        
        #récupération de la distance entre les 2 adresses 
        total_distance = self.server_rest.get_distance(coord_d_add,coord_a_add)
        
        #récupération du nombre d'arret 
        nbr_stop = self.server_rest.get_nbr_stop(total_distance,autonomie)
        
        #récupération des distances d'arrets
        list_stop = self.server_rest.get_coodinates_end_auto(coord_d_add,coord_a_add,nbr_stop)
        
        #récupération des coordonnées bornes d'arrets 
        coord_bornes_stop = self.server_rest.get_bornes(list_stop,1000)
        
        #récupération des adresses des bornes d'arrets 
        adds_bornes_stop = []
        
        for bornes in coord_bornes_stop:
            add_borne_stop = self.server_rest.get_address(bornes[0],bornes[1])
            adds_bornes_stop.append(add_borne_stop)
               
        return adds_bornes_stop
    
    def get_nbr_stop(self,depart_add, arriv_add, autonomie):
        
        #récupération des coordonnées des adresses de départ et d'arrivée
        coord_d_add = self.server_rest.get_coordinates(depart_add)
        coord_a_add = self.server_rest.get_coordinates(arriv_add)
        
        #récupération de la distance entre les 2 adresses 
        total_distance = self.server_rest.get_distance(coord_d_add,coord_a_add)
        
        #récupération du nombre d'arret 
        nbr_stop = self.server_rest.get_nbr_stop(total_distance,autonomie)
        
        return nbr_stop
    
    def get_total_distance(self,depart_add, arriv_add):
        
        #récupération des coordonnées des adresses de départ et d'arrivée
        coord_d_add = self.server_rest.get_coordinates(depart_add)
        coord_a_add = self.server_rest.get_coordinates(arriv_add)
            
        #récupération de la distance entre les 2 adresses 
        total_distance = self.server_rest.get_distance(coord_d_add,coord_a_add)
        
        return total_distance
        
        
            
# =============================================================================
# MAIN
# =============================================================================
#rest_manager =Rest_manager()

#adr2 = "88, chemin d'en Bernard, 74380 Cranves-Sales"
#adr1 = "Paris"
#adr1 = "18, allée du Perthuis, 74940 Annecy-le-Vieux"
#adr1 = "67, rue Salomon Reinach, 69007 Lyon"

#print (rest_manager.get_bornes_address(adr1, adr2, 40))
#print (rest_manager.get_nbr_stop(adr1, adr2,50))
#print (rest_manager.get_total_distance(adr1, adr2))





