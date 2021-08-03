from bottle import route, template, get, post, request
#from playhouse.shortcuts import model_to_dict
from connection import *

@get('/home')
def home():
    return  template('index')

@get('/registrar_autor')
def registrar_autor():
    return '''
        <form action="/registrar_autor" method="post">
            full_name: <input name="full_name" type="text"/>
            user: <input name="user" type="text" />
            password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/registrar_autor')
def registrar():
    full_name = request.forms.get('full_name')
    user = request.forms.get('user')
    password = request.forms.get('password')
    return create_author(full_name, user, password)

@get('/login')
def login():
    return '''
        <form action="/login" method="post">
            user: <input name="user" type="text" />
            password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login')
def do_login():
    user = request.forms.get('user')
    password = request.forms.get('password')
    return check_login(user, password)

@post('/notes/<user>')
def notes(user):
    author = read_author_user(user)
    record = read_note_author(author)
    return record

@get('/new_note')
def new_note():
    return '''
        <form action="/new_note" method="post">
            usuario: <input name="usuario" type="text" />
            titulo: <input name="titulo" type="text" />
            contenido: <input name="contenido" type="text" />
            <input value="New Note" type="submit" />
        </form>
    '''

@post('/new_note')
def do_new_note():
    user = request.forms.get('usuario')
    title = request.forms.get('titulo')
    content = request.forms.get('contenido')
    author = read_author_user(user)
    return create_note(title, content, author)

@get('/all_notes')
def all_notes():
    record = read_note_all()
    return record