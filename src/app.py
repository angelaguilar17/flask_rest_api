from flask import Flask
from config import config 

#importar rutas

from routes import wheather

app = Flask(__name__)

def page_no_found(error):
    return "<h1>Not found page</h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(wheather.main,url_prefix='/api/wheater')
    
    #error handlers
    app.register_error_handler(404,page_no_found)
    app.run()

