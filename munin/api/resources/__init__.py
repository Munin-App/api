from munin.api.resources.ping import PingResource
from munin.api.resources.token import TokenResource
from munin.api.resources.locations import LocationResource

endpoints = [
    ('/ping/', PingResource()),
    ('/tokens/', TokenResource()),
    ('/locations/', LocationResource())
]
