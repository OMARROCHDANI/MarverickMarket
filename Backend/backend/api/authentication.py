from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_framework.authtoken.models import Token
# we've done overriding
class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'