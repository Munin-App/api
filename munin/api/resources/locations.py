import falcon
from munin.models import Token, Location
import json


class LocationResource(object):
    def on_post(self, req, resp):
        try:
            latitude = req.params['latitude']
            longitude = req.params['longitude']
            timestamp = req.params['timestamp']
        except KeyError as e:
            raise falcon.HTTPBadRequest('Missing parameter', str(e))

        token = req.get_header('X-Authorization')

        if token is None:
            resp.status = falcon.HTTP_401
            return

        token = Token.authenticate(token)

        if token is None:
            resp.status = falcon.HTTP_401

        try:
            location = Location.add(token_id=token.id, latitude=latitude,
                                    longitude=longitude, timestamp=timestamp)

            resp.body = str(location.id)
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.body = json.dumps({'error': str(e)})
