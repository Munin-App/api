from peewee import Model, SqliteDatabase
from munin.models import database

class Model(Model):

    class Meta:
        database = database
