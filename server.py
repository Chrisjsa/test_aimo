from bottle import run
from connection import *
from controller import *
# Start your code here, good luck (: ...

db.connect()
db.create_tables([Author, Note], safe=True)
db.close()

run(host='localhost', port=8000)