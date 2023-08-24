from flask import Flask, render_template
from rutas.routes import configure_routes
from conexion.db_connection import create_db_connection

app = Flask(__name__)


mysql = create_db_connection(app)
configure_routes(app)







@app.route('/')
def hola():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)
