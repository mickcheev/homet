from fastapi import Response, status

from main import app

from notes.services.manage_notes import get_notes_list as get_notes
from users.models import User
from users.entities import UserRegistration
from users.services.register_user import register_user as registrer, db_to_entity
from users.exceptions import UserAlreadyExists


@app.get('/')
def server_status():
    return {'status': 'ok'}


@app.get('/notes')
def get_notes_list():
    return get_notes(user=User.get(User.email == 'mikacha'))


@app.post('/register', status_code=201)
def register_user(user: UserRegistration, response: Response):
    try:
        result = db_to_entity(registrer(user))
    except UserAlreadyExists:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'Error': "User with the same email already exists"}
    return result


