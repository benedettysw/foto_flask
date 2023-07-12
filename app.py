from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'foto'
mysql = MySQL(app)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        foto = request.files['foto']
        imagen_data = foto.read()
        sql = mysql.connection.cursor()
        sql.execute('INSERT INTO registro (nombre, apellido, foto) VALUES (%s, %s, %s)',
                    (nombre, apellido, imagen_data))
        mysql.connection.commit()
        imagen_id = sql.lastrowid
        imagen_url = url_for('mostrar_imagen', imagen_id=imagen_id)
        return render_template('template.html', imagen_url=imagen_url)


@app.route('/mostrar_imagen/<int:imagen_id>')
def mostrar_imagen(imagen_id):
    sql = mysql.connection.cursor()
    sql.execute('SELECT foto FROM registro WHERE id = %s', (imagen_id,))
    imagen_data = sql.fetchone()[0]

    # Devuelve la imagen con el tipo de contenido adecuado
    response = make_response(imagen_data)
    response.headers.set('Content-Type', 'image/jpeg')  # Ajusta el tipo de contenido según corresponda

    return response


@app.route('/')
def hola():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
