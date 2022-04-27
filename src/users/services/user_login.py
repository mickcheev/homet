from peewee import DoesNotExist

from users.models import User
from users.entities import UserLogin, UserRegistration
from users.exceptions import InvalidUserData
from users.services import passwords_manage


def login_user(user: UserLogin | UserRegistration):
    try:
        db_user = User.get(User.email == user.email)
    except DoesNotExist:
        raise InvalidUserData
    else:
        if db_user.password != passwords_manage.hash_password(user.password):
            raise InvalidUserData
        return db_user
