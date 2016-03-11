import json
import falcon
from munin.models import User, Token


class TokenResource(object):
    def on_post(self, req, resp):
        try:
            username = req.params['username']
            password = req.params['password']
            name = req.params['name']
            read_only = req.params.get('read_only', True)
        except KeyError as e:
            raise falcon.HTTPBadRequest('Missing parameter', str(e))

        user = User.authenticate(username, password)

        if user:
            if type(read_only) == str:
                if read_only.lower() in ['true', 'yes']:
                    read_only = True
                else:
                    read_only = False
            else:
                read_only = False

            try:
                token = Token.add(user_id=user.id, name=name, read_only=read_only)

                resp.body = json.dumps(token.serializeToJSON())
            except Exception as e:
                raise falcon.HTTPInternalServerError('Error', str(e))
        else:
            resp.status = falcon.HTTP_401
