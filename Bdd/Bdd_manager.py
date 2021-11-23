# =============================================================================
# IMPORT
# =============================================================================
from Query import Query


class Bdd_manager():

# =============================================================================
# CONSTRUCTEUR
# =============================================================================
     def __init__(self):
         self.query = Query()
        
# =============================================================================
# FONCTIONS
# =============================================================================
     def bdd_launcher(self):
         bdd_result = self.query.get_bdd()
         return bdd_result
     
     def get_autonomie(self, name_voiture):
         autonomie_result = self.query.get_autonomie(name_voiture)
         return autonomie_result
     
     def get_tempsChargement(self, name_voiture):
         tempsChargement = self.query.get_tempsChargement(name_voiture)
         return tempsChargement

# =============================================================================
# MAIN
# =============================================================================
#bdd_manager =Bdd_manager()
#print (bdd_manager.bdd_launcher())
#print (bdd_manager.get_autonomie('Mustang'))
#print (bdd_manager.get_tempsChargement('Mustang'))
