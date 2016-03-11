import falcon
from munin.models import Token, Location
import json
import datetime


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

    def on_get(self, req, resp):
        limit = req.params.get('limit', 100)
        offset = req.params.get('offset', 0)
        token = req.get_header('X-Authorization', req.params.get('token', None))

        if token is None:
            resp.status = falcon.HTTP_401
            return

        token = Token.authenticate(token)

        if token is None:
            resp.status = falcon.HTTP_401
            return

        try:
            locations = Location.select().where(Location.user_id == token.user_id)

            response = {
                'meta': {
                    'offset': offset,
                    'limit': limit,
                    'total': Location.select().count()
                },
                'locations': []
            }

            for location in locations.offset(offset).limit(limit):
                response['locations'].append({
                    'latitude': location.latitude,
                    'longitude': location.longitude,
                    'timestamp': datetime.datetime.strftime(location.timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
                })

            resp.body = json.dumps(response)
        except:
            resp.status = falcon.HTTP_500
