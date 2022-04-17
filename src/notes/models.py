from datetime import date

from peewee import SqliteDatabase, Model, CharField, DateField, ForeignKeyField,\
        IntegerField, TextField

from config import DB_PATH
from users.models import User


db = SqliteDatabase(DB_PATH)


class Note(Model):
    id = IntegerField(primary_key=True)
    author = ForeignKeyField(User)
    title = CharField(max_length=120)
    creation_date = DateField(default=date.today)
    last_change_date = DateField(default=date.today())
    content = TextField(null=True)
    permission = IntegerField(default=2)
    # 1 means that note can be reded not only by author
    # 2 means that note can be readed only by the author


    class Meta:
        database = db
        table_name = 'User'



