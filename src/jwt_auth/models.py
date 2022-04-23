from datetime import date, timedelta
from random import choice, randint

from peewee import SqliteDatabase, Model, CharField, DateField, IntegerField, ForeignKeyField

from config import DB_PATH

from users.models import User


db = SqliteDatabase(DB_PATH)


def get_random_word() -> str:
    word = ''
    for i in range(randint(2, 25)):
        word += choice(['a', 'b', 'c'])


class Jwt_key(Model):
    id = IntegerField(primary_key=True)

    # start payload
    app_name = 'Homet'
    date_until = DateField(default=date.today()+timedelta(days=1))
    random_word = CharField(100, default=get_random_word)
    # end payload

    recovery_key = CharField(128)
    user = ForeignKeyField(User)

    class Meta:
        database = db
        table_name = 'Jwt key'
