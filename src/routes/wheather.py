from flask import Blueprint, jsonify
#importar modelos

from models.WheaterModel import WheaterModel
main=Blueprint('wheather_blueprint',__name__)

@main.route('/') #ruta principal
def get_wheater(): #obtiene
    try:
        wheaters = WheaterModel.get_wheaters()
        return jsonify(wheaters)
    
    except Exception as ex:

        return jsonify({'message':str(ex)}),500
