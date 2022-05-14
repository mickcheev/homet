from peewee import SqliteDatabase

from config import DB_PATH

from notes.models import Node, Note
from users.models import User, TelegramUserKey
from media.models import Picture, Audio
from jwt_auth.models import Jwt_key

db = SqliteDatabase(DB_PATH)


def create_database():
    with db:
        db.create_tables([User, Note, Node, Audio, Picture, Jwt_key, TelegramUserKey])
