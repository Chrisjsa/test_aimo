from peewee import *
import json
import datetime

db = SqliteDatabase("test.db")

class BaseModel(Model):
    class Meta:
        database=db

class Author(BaseModel):
    full_name = CharField()
    user = CharField(unique=True)
    password = CharField()

def create_author(full_name, user, password):
    insert = Author.insert(full_name=full_name, user=user, password=password).execute()
    author = read_author_id(insert)
    return author

def read_author_all():
    back = json.dumps(list(Author.select().dicts()))
    return back

def read_author_id(id):
    back = json.dumps(list(Author.select().where(Author.id == id).dicts()))
    return back

def read_author_name(full_name):
    back = Author.get(Author.full_name == full_name)
    return back

def read_author_user(user):
    back = Author.get(Author.user == user)
    return back

def check_login(user, password):
    back = Author.get(Author.user == user, Author.password == password)
    autor = {
        'Autor': Author.full_name
    }
    return autor

class Note(BaseModel):
    time = str(datetime.datetime.now())
    author = ForeignKeyField(Author, backref='notes')
    title = CharField()
    content = TextField()
    created_date = CharField(default=time)

def create_note(title, content, author):
    insert = Note.insert(title=title, content=content, author=author).execute()
    note = read_note_id(insert)
    return note

def read_note_all():
    back = json.dumps(list(Note.select().dicts()))
    return back

def read_note_id(id):
    back = json.dumps(list(Note.select().where(Note.id == id).dicts()))
    return back

def read_note_title(title):
    back = json.dumps(list(Note.select().where(Note.title == title).dicts()))
    return back

def read_note_author(author):
    back = json.dumps(list(Note.select().where(Note.author ==  author).dicts()))
    return back