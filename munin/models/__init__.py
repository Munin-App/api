from peewee import SqliteDatabase

database = SqliteDatabase('munin.db')

from munin.models.model import Model
from munin.models.user import User
from munin.models.token import Token

database.create_tables([User, Token], safe=True)
