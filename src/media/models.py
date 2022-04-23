from peewee import SqliteDatabase, Model, CharField, DateField, IntegerField

from config import DB_PATH


db = SqliteDatabase(DB_PATH)


class Picture(Model):
    id = IntegerField(primary_key=True)
    path = CharField(max_length=300)

    class Meta:
        database = db
        table_name = 'Picture'


class Audio(Model):
    id = IntegerField(primary_key=True)
    path = CharField(max_length=300)

    class Meta:
        database = db
        table_name = 'Audio'
