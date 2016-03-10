import falcon
from munin.api.resources import endpoints

server = falcon.API()

for endpoint in endpoints:
    server.add_route(endpoint[0], endpoint[1])
