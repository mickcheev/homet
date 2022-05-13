from datetime import date

from peewee import SqliteDatabase, Model, CharField, DateField, ForeignKeyField,\
        IntegerField, TextField, BooleanField, DoesNotExist

from config import DB_PATH
from users.models import User


db = SqliteDatabase(DB_PATH)


class Node(Model):
    """
    This model realizes the directory function
    to bind the notes
    """

    # prime means that it's the root directory
    # that any user has by default
    prime = BooleanField(default=False)
    parent = IntegerField(null=True)
    owner = ForeignKeyField(User)
    name = CharField(max_length=40)

    class Meta:
        database = db
        table_name = 'Node'


class Note(Model):
    author = ForeignKeyField(User)
    title = CharField(max_length=120)
    creation_date = DateField(default=date.today)
    last_change_date = DateField(default=date.today())
    content = TextField(null=True)

    # 1 means that note can be read not only by author
    # 2 means that note can be read only by the author
    permission = IntegerField(default=2)

    node = ForeignKeyField(Node)

    class Meta:
        database = db
        table_name = 'Note'
