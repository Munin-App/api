import os
from peewee import PostgresqlDatabase

database = PostgresqlDatabase(os.environ['munin_db_name'],
                              user=os.environ['munin_db_user'],
                              password=os.environ['munin_db_password'],
                              host=os.environ['munin_db_host'])

from munin.models.model import Model
from munin.models.user import User
from munin.models.token import Token
from munin.models.location import Location

database.create_tables([User, Token, Location], safe=True)
