# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:58:34 2021

@author: Mbrt_
"""

# =============================================================================
# Import
# =============================================================================

import requests
from math import *
import urllib.parse
import ast
import haversine as hs


class Server_Rest():
    
# =============================================================================
#     CONSTRUCTEUR
# =============================================================================
    def __init__(self):
         pass

# =============================================================================
#   FONCTIONS
# =============================================================================

    def get_coordinates(self,adr):
        #Récupération de coordonnées par rapport à une adresse
    
        #appel de l'API
        api_url = "https://api-adresse.data.gouv.fr/search/?q="
        adr = adr
        r = requests.get(api_url + urllib.parse.quote(adr))
        
        #Parsing des coordonnées 
        dico_data = ast.literal_eval(r.content.decode('unicode_escape'))
        coordinates = dico_data['features'][0]['geometry']['coordinates']
        longitude = coordinates[0]
        latuditude = coordinates[1]
        
        return(latuditude,longitude)
    
    
    def get_address(self, latitude, longitude):
        #récupération d'une adresse par rapport à des coordonnées
        
        #appel de l'API
        api_url = f"https://api-adresse.data.gouv.fr/reverse/?lon={longitude}&lat={latitude}"
        response = requests.get(api_url)
        response= response.json()
        
        #Parsing des coordonnées 
        address = response['features'][0]['properties']['label']
        
        return address
        
        
    def get_distance(self,distance1,distance2):
        
        loc1 = (distance1)
        loc2 = (distance2)
        
        #Récupèration la distance en km
        total_distance = ceil(hs.haversine(loc1,loc2)) 
        
        return (total_distance)
        
    def get_nbr_stop(self,total_distance,autonomie):
        
        #Calcul en combien le trajet dois etre divisé avec l'autonomie de la voiture
        slot_distance = ceil(total_distance/ (autonomie -20))
        
        return slot_distance
    
    
    def get_coodinates_end_auto(self,distance1,distance2,slot_distance):
        #Récupère la liste des points de fin d'autonomie
        
        #Calcul du point de coordonnée entre la distance 1 et 2 
        total_cordinates =[]
        total_cordinates.append(abs(distance1[0] - distance2[0]))
        total_cordinates.append(abs(distance1[1] - distance2[1]))
        
        #Calcul du point à ajouter a nos distance (point d'un slot)
        total_cordinates_slot=[]
        total_cordinates_slot.append(abs(total_cordinates[0]/slot_distance))
        total_cordinates_slot.append(abs(total_cordinates[1]/slot_distance))
            
        list_autonomie = []
        #Ajout des points de coordonnée trouver a notre point de départ.
        for i in range (1,slot_distance+1):
            
            end_automonie_cordinates = []
            
            #Calcul de la lattitude
            if distance1[0]>distance2[0]:
                end_automonie_cordinates.append(round(distance1[0] - (total_cordinates_slot[0]*i),6))
            
            else :
                 end_automonie_cordinates.append(round(distance1[0] + (total_cordinates_slot[0]*i),6))
            
            #Calcul de la longitude
            if distance1[1]>distance2[1]:
                end_automonie_cordinates.append(round(distance1[1] - (total_cordinates_slot[1]*i),6))
        
            else :
                end_automonie_cordinates.append(round(distance1[1] + (total_cordinates_slot[1]*i),6))
             
            #Ajout des point trouvé à la liste
            list_autonomie.append(end_automonie_cordinates)
      
        return(list_autonomie)
    
    
    
    def get_bornes(self,list_coordinates,perimetre):
        #Récupère la liste de coordonnées des bornes d'arrets
        
        list_bornes = []               
        
        for list in list_coordinates:
            
            result=0
            
            while result==0:
                # appel l'api et récupère les bornes autour d'un périmètre donnée
                url_api =f"https://opendata.reseaux-energies.fr/api/records/1.0/search/?dataset=bornes-irve&q=&rows=1&facet=region&geofilter.distance={list[0]}%2C{list[1]}%2C{perimetre}"
                response = requests.get(url_api)
                response= response.json()
                
                #Imcrémente le périmetre de recherche de 1km si pas de bornes sont trouvées
                if response['nhits'] ==0:
                    perimetre = perimetre + 1000
                    
                else: 
                    result=1
            else:
                #Récupération lattitue, longitude
                latitude = format(response['records'][0]['fields']['ylatitude'],'.6f')
                longitude = format(response['records'][0]['fields']['xlongitude'],'.6f')
            
                list_bornes.append([latitude,longitude])
            
        return list_bornes

            
# =============================================================================
# Main 
# =============================================================================

#server_rest = Server_Rest() 

# adr1 = "88, chemin d'en Bernard, 74380 Cranves-Sales"
# #adr2 = "Paris"
# #adr1 = "18, allée du Perthuis, 74940 Annecy-le-Vieux"
# adr2 = "67, rue Salomon Reinach, 69007 Lyon"

# distance1 = server_rest.get_coordinates(adr1)
# distance2 = server_rest.get_coordinates(adr2)
# print(distance1, distance2)

# total_distance= server_rest.get_distance(distance1,distance2)
# print(total_distance)

# list_autonomie = server_rest.get_coodinates_end_auto(distance1,distance2,total_distance)
# print(list_autonomie)

# d1 = 45.750026
# d2 = 5.750026
# d = 10000

# coordinates_borne = server_rest.get_bornes(list_autonomie, d)
# print (coordinates_borne)


#print (server_rest.get_address(45.803378,5.111916))
#print(server_rest.get_address(46.191120,6.317650))