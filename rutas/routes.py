from flask import request
from conexion.db_connection import create_db_connection

def configure_routes(app):
    mysql = create_db_connection(app)

    @app.route('/add', methods=['POST'])
    def add():
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellido = request.form['apellido']
        

            sql = mysql.connection.cursor()
            sql.execute('INSERT INTO registro (nombre, apellido) VALUES (%s, %s)',
                        (nombre, apellido))

            mysql.connection.commit()
            return "ok" 
        

