from peewee import DoesNotExist

from users.entities import UserRegistration
from users.models import User as DbModel
from users.exceptions import UserAlreadyExists
from users.services.passwords_manage import hash_password


def check_existence(user: UserRegistration) -> None:
    try:
        DbModel.get(DbModel.email == user.email)
    except DoesNotExist:
        pass

    else:
        raise UserAlreadyExists


def register_user(user: UserRegistration) -> DbModel:
    check_existence(user)

    return DbModel.create(
        email=user.email, first_name=user.first_name,
        second_name=user.second_name, password=hash_password(user.password),
        telegram_account=user.telegram_account,
    )