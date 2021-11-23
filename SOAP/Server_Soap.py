# =============================================================================
# IMPORT
# =============================================================================

from spyne import Application, rpc, ServiceBase, Unicode, Iterable, Integer
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import  Soap11
from math import *


class Server_Soap(ServiceBase):

# =============================================================================
# FONCTIONS
# =============================================================================
                
    @rpc(Integer, Integer, Integer, _returns=(Integer))
    def get_temps_trajet(ctx,total_distance,nbr_stop, temps_chargement):
        
        #Calcul du temps de trajet 
        # On considère que la voiture roule à 70 km/h en moyenne 
        trip_time = ceil((total_distance*60)/70) + ((nbr_stop-1)*temps_chargement)
        
        return trip_time
      

# =============================================================================
# SERVER
# =============================================================================


application = Application([Server_Soap], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application) # server


from wsgiref.simple_server import make_server
server = make_server('127.0.0.1', 8000, wsgi_application)
server.serve_forever()