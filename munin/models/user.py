from munin.models import database
import bcrypt


class User(object):

    @staticmethod
    def create(username, password):
        query = 'INSERT INTO users (username, password) VALUES(:username, :password)'

        username = username.encode('utf-8')
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        database.query(query, username=username, password=password)
