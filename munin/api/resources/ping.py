import json


class PingResource(object):
    def on_get(self, req, resp):
        response = {
            'response': 'pong'
        }

        resp.body = json.dumps(response)
