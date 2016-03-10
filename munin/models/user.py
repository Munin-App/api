from munin.models import database
import bcrypt


class User(object):

    @staticmethod
    def create(username, password):
        query = 'INSERT INTO users (username, password) VALUES(:username, :password)'

        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        password = password.decode('utf-8')

        database.query(query, username=username, password=password)

    @staticmethod
    def authenticate(username, password):
        query = 'SELECT password FROM users WHERE username=:username'

        try:
            hashed_password = database.query(query, username=username).all()[0].password

            if bcrypt.hashpw(password.encode('utf-8'), hashed_password.encode('utf-8')) == hashed_password.encode('utf-8'):
                return True
        except Exception as e:
            raise e

        return False
