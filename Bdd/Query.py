# =============================================================================
# IMPORT
# =============================================================================
import requests as rq
import json


class Query():

# =============================================================================
# Constructeur
# =============================================================================
    def __init__(self):
        pass
    
# =============================================================================
# FONCTIONS
# =============================================================================

    def get_bdd(self):
        query = """
            {
              allVoitures{
                edges{
                  node{
                    name
                    marque
                    autonomie
                    tempsChargement
                  }
                }
              }
            }"""
    
        #lance la query sur notre serveur graphql et recupère le resulat
        response = rq.post("http://127.0.0.1:5000/graphql", json={"query": query})
        
        #transforme du texte en dico
        json_response = json.loads(response.text)
        
        return(json_response)
    
    
    def get_autonomie(self, name_voiture):
        
        # Récupération du contenu de la bdd
        bdd_content = self.get_bdd()
        cars = bdd_content['data']['allVoitures']['edges']
        
        # Boucle pour récupérer l'autonimie et le temps de chargement pour la voirture choisie 
        for car in cars:
            if car['node']['name'] == name_voiture:
                return (car['node']['autonomie'])
            else:
                #Ce n'est pas cette voiture
                pass
     
     
    def get_tempsChargement(self, name_voiture):
        
         # Récupération du contenu de la bdd
        bdd_content = self.get_bdd()
        cars = bdd_content['data']['allVoitures']['edges']
        
        # Boucle pour récupérer l'autonimie et le temps de chargement pour la voirture choisie 
        for car in cars:
            if car['node']['name'] == name_voiture:
                return (car['node']['tempsChargement'])
            else:
                #Ce n'est pas cette voiture
                pass


# =============================================================================
# MAIN
# =============================================================================

# query = Query()
# print (query.get_autonomie('Mustang'))
# print (query.get_tempsChargement('Mustang'))