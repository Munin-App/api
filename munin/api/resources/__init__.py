from munin.api.resources.ping import PingResource
from munin.api.resources.token import TokenResource

endpoints = [
    ('/ping/', PingResource()),
    ('/tokens/', TokenResource())
]
