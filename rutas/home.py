from flask import Blueprint, render_template , render_template


routes_home = Blueprint("routes_home", __name__)

#ruta del formulario
@routes_home.route('/foto', methods=['GET'])
def formularios():
    return render_template('template.html')
