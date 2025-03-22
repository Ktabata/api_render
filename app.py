from flask import Flask, jsonify, request
from pickle import load as pload
app = Flask(__name__)

#Crear el servicio:
#1 Cargar el archivo con with que se encarga de abrir y cerrar el archivo
with open('model_dict_car_eval_rf.pkl','rb') as file:
    model_dict = pload(file)

@app.route('/', methods=['POST'])
def predict_car_evaluation():
    if request.methods == 'POST':
        data = request.GET__json()
        buying = data.GET('buying')
        maint = data.GET('maint'), 
        doors = data.GET('doors')
        persons = data.GET('persons') 
        lug_boot = data.GET('lug_boot')
        safety = data.GET('safety')