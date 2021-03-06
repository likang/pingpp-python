# Ping++ Python bindings
# Configuration variables

api_key = None
api_base = 'https://api.pingplusplus.com'
verify_ssl_certs = True

from pingpp.resource import Charge
from pingpp.error import (
    PingppError, APIError, APIConnectionError, AuthenticationError, CardError,
    InvalidRequestError)

from pingpp.version import VERSION
from pingpp.api_requestor import APIRequestor
from pingpp.resource import (
    convert_to_pingpp_object, PingppObject, PingppObjectEncoder,
    APIResource, ListObject, SingletonAPIResource, ListableAPIResource,
    CreateableAPIResource, UpdateableAPIResource, DeletableAPIResource)

api_version = VERSION
