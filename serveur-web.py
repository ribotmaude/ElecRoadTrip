# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 22:47:58 2021

@author: Mbrt_
"""
# =============================================================================
# IMPORT
# =============================================================================

from flask import Flask, render_template, request, redirect
import sys
sys.path.append("static/app")

from Bdd_manager import Bdd_manager
from Rest_manager import Rest_manager
from Soap_manager import Soap_manager


app = Flask(__name__)

# =============================================================================
# ROUTES
# =============================================================================
@app.route('/')
@app.route('/home')
def home():
    return render_template('/html/home.html')

@app.route('/planyourtrip')
def planyourtrip():
    cars = bdd_manager.bdd_launcher()   
    cars = cars['data']['allVoitures']['edges']
    return render_template('/html/planyourtrip.html', cars=cars)

@app.route('/fill_form', methods=['POST'])
def fill_form():
    #recupérartion du formulaire
    rqst= request.form
    
    #récupartion des champs
    car_name = rqst['car_name']
    departure_address = rqst['departure']
    arrival_address = rqst['arrival']
    
    #Recupération du temps de chargement + autonomie
    autonomie = bdd_manager.get_autonomie(car_name)
    tempsChargement = bdd_manager.get_tempsChargement(car_name)
    
    #récupération du temps de trajet
    nbr_stop = rest_manager.get_nbr_stop(departure_address, arrival_address,autonomie)
    total_distance = rest_manager.get_total_distance(departure_address, arrival_address)
    total_trip_time = soap_manager.get_soap_distance(total_distance, nbr_stop, tempsChargement)
    
    #récupartion de l'emplacement des bornes d'arret        
    address_bornes_stop = rest_manager.get_bornes_address(departure_address, arrival_address, autonomie)    
    
        
    return render_template('/html/fill_form.html',car_name=car_name, departure_address= departure_address, arrival_address=arrival_address, autonomie=autonomie,nbr_stop=nbr_stop, address_bornes_stop=address_bornes_stop, total_trip_time=total_trip_time )
    


@app.route('/ourcars')
def ourcars():
    cars = bdd_manager.bdd_launcher()   
    cars = cars['data']['allVoitures']['edges']
    return render_template('/html/ourcars.html', cars=cars)

@app.route('/about')
def about():
    return render_template('/html/about.html')


# =============================================================================
# main
# =============================================================================
if __name__ == "__main__":
    bdd_manager = Bdd_manager()
    rest_manager = Rest_manager()
    soap_manager = Soap_manager()
    app.run(host='127.0.0.1', port='1000')