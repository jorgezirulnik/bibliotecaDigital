from flask import Flask, render_template, request, redirect, send_from_directory, session, flash, url_for, jsonify
from datetime import datetime
from werkzeug.utils import secure_filename
from wtforms import StringField, DateField, SelectField
from wtforms.validators import DataRequired
import os

app=Flask(__name__)

# Ruta donde se guardarán los archivos
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'docx'}

UPLOAD_FOLDER = 'static/img/'

app.config['UPLOAD_FOLDER_ESTUDIOS'] = UPLOAD_FOLDER + 'estudios/'

app.config['UPLOAD_FOLDER_MEDICAMENTOS'] = UPLOAD_FOLDER + 'medicamentos/'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def allowed_file(filename_medicamentos):
    return '.' in filename_medicamentos and filename_medicamentos.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def admin_login():
    return render_template('sitio/index.html')

#@app.route('/', methods=['POST'])
#def admin_login_post():
#    _usuario = request.form['txtUsuario']
#    _password = request.form['txtPassword']
#
#    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#    cur.execute("SELECT * FROM usuarios WHERE nombreUsu = %s", (_usuario,))
#    user = cur.fetchone()
#    cur.close()
#
#    if user and check_password_hash(user['claveUsu'],_password):
#        session['login'] = True
#        session['usuario'] = user['idUsuario']
#        session['nombreUsu'] = user['nombreCompleto']
#        session['perfil'] = user['idPerfil']
#        session['clave'] = user['claveUsu']
#        return redirect('/index.html')
#
#    return render_template('admin/login.html', mensaje="Usuario o clave incorrecto. Acceso denegado")


@app.route('/admin/indexSeguridad')
def seguridad():
    if not 'login' in session or session['perfil'] != 1:
        return redirect('/index.html')

    return render_template('/admin/indexSeguridad.html', usuNombre=session['nombreUsu'])

@app.route('/index.html')
def inicio():
    return render_template('/sitio/index.html', usuNombre=session['nombreUsu'])

if __name__ == '__main__':
    app.run(debug=True)

