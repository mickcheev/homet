from datetime import date

from peewee import SqliteDatabase, Model, CharField, DateField

from config import DB_PATH


db = SqliteDatabase(DB_PATH)


class User(Model):
    first_name = CharField(max_length=30)
    second_name = CharField(max_length=30)
    email = CharField(max_length=30, primary_key=True)
    password = CharField(max_length=128)
    accession_date = DateField(default=date.today)
    telegram_account = CharField(max_length=30,  null=True)

    class Meta:
        database = db
        table_name = 'User'



