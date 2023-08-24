from flask_mysqldb import MySQL
from conexion.db_config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from flask import Flask


def close_db_connection(mysql):
    mysql.connection.close()


def create_db_connection(app: Flask):
    app.config['MYSQL_HOST'] = MYSQL_HOST
    app.config['MYSQL_USER'] = MYSQL_USER
    app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
    app.config['MYSQL_DB'] = MYSQL_DB
    mysql = MySQL(app)
    return mysql
