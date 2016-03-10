import datetime

import bcrypt
from peewee import CharField, DateTimeField

from munin.models import Model


class User(Model):
    username = CharField(unique=True)
    password = CharField()
    created = DateTimeField(default=datetime.datetime.utcnow())

    @staticmethod
    def add(username, password):
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        password = password.decode('utf-8')

        user = User.create(username=username, password=password)

        return user

    @staticmethod
    def authenticate(username, password):
        try:
            user = User.get(User.username == username)
            password = password.encode('utf-8')
            computed = user.password.encode('utf-8')

            if bcrypt.hashpw(password, computed) == computed:
                return user
        except User.DoesNotExist:
            pass

        return None
