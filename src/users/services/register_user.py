from secrets import token_hex

from peewee import DoesNotExist

from users.entities import UserRegistration
from users.models import User as DbModel, TelegramUserKey
from users.exceptions import UserAlreadyExists
from users.services.passwords_manage import hash_password
from notes.services.manage_nodes import create_node, create_prime_node


def check_existence(user: UserRegistration) -> None:
    try:
        DbModel.get(DbModel.email == user.email)
    except DoesNotExist:
        pass

    else:
        raise UserAlreadyExists


def register_user(user: UserRegistration) -> DbModel:
    check_existence(user)

    db_user = DbModel.create(
        email=user.email, first_name=user.first_name,
        second_name=user.second_name, password=hash_password(user.password),
        telegram_account=user.telegram_account,
    )
    create_prime_node(db_user)
    TelegramUserKey.create(user=db_user, key=str(token_hex(32)))
    return db_user


def delete_user(user_email: str):
    DbModel.delete().where(DbModel.email == user_email).execute()
