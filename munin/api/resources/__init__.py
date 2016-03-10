from munin.api.resources.ping import PingResource

endpoints = [
    ('/ping/', PingResource())
]
