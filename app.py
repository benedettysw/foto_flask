from flask import Flask, render_template , request
from flaskext.mysql import MySQL
from datetime import datetime

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'desdecero'
mysql.init_app(app)





@app.route('/add', methods=['POST'])
def add():
    nombre = request.form['nombre']
    apellido = request.form['apellido']

    # Obtener una conexión
    con = mysql.connect()
    cursor = con.cursor()

    # Realizar operaciones con la base de datos
    cursor.execute('INSERT INTO registro (nombre, apellido) VALUES (%s, %s)',
                   (nombre, apellido))
    con.commit()

    # Cerrar cursor y conexión
    cursor.close()
    con.close()

    return "ok"










@app.route('/registrar', methods=['POST'])
def registro():
    nombre = request.form['nombre']
    email = request.form['email']
    clave = request.form['claves']

    # Obtener una conexión
    con = mysql.connect()
    cursor = con.cursor()

    # Realizar operaciones con la base de datos
    cursor.execute('INSERT INTO registro (nombre, email, clave) VALUES (%s, %s,%s)',
                   (nombre, email , clave))
    con.commit()

    # Cerrar cursor y conexión
    cursor.close()
    con.close()

    return "ok"


    



@app.route('/')
def hola():
    return render_template('index.html')




@app.route('/datos')
def datos():
    return render_template('registro.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)