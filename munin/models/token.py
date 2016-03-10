from munin.models import database
import uuid


class Token(object):

    @staticmethod
    def create(user_id, name, read_only=True):
        query = 'SELECT COUNT(*) FROM users WHERE id=:user_id'

        if database.query(query, user_id=user_id)[0][0] == 0:
            raise Exception('User does not exist')

        token = None
        exists = True

        while exists:
            token = uuid.uuid4().hex

            query = 'SELECT COUNT(*) FROM tokens WHERE token=:token'

            if database.query(query, token=token)[0][0] == 0:
                exists = False

        query = 'INSERT INTO tokens (token, name, read_only, user_id) VALUES(:token, :name, :read_only, :user_id)'

        database.query(query, token=token, name=name,
                       read_only=read_only, user_id=user_id)
