from munin.models import Model, User
from peewee import CharField, DateTimeField, BooleanField, ForeignKeyField
import os
import hashlib
import datetime


class Token(Model):
    token = CharField(unique=True)
    name = CharField()
    created = DateTimeField(default=datetime.datetime.utcnow())
    last_used = DateTimeField(null=True)
    read_only = BooleanField(default=True)
    user = ForeignKeyField(User, related_name='tokens')

    @staticmethod
    def add(user_id, name, read_only=True):
        token = hashlib.sha256(os.urandom(256)).hexdigest()

        while Token.select().where(Token.token == token).count() != 0:
            token = hashlib.sha256(os.urandom(256)).hexdigest()

        try:
            token = Token.create(token=token, name=name, read_only=read_only,
                                 user=User.get(User.id == user_id))

            return token
        except User.DoesNotExist:
            pass

        return None

    @staticmethod
    def authenticate(token):
        try:
            token = Token.get(Token.token == token)

            return token.user
        except Token.DoesNotExist:
            pass

        return None
