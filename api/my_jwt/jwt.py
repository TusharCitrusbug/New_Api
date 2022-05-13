
import base64
import random
import string
import json
import random
from rest_framework.authentication import BasicAuthentication,get_authorization_header
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import HTTP_HEADER_ENCODING, exceptions

def my_key():
    length=random.randint(0, 20)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def my_encode(payload):
        key=my_key()
        payload=json.dumps(payload)
        secrate=random.randint(0, 343432273872874823742734827384734243)
        new_payload = f'{key}mahan_raja{payload}mahan_raja{secrate}'
        message_bytes = new_payload.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return (f'{base64_message}payload_key{secrate}')


def my_decode(token):
    
        token=token.split('payload_key')[0]
        base64_bytes = token.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii') 
        message=json.loads(message.split('mahan_raja')[1])
        return message

def get_my_authorization_header(request):

    auth = request.META.get('HTTP_AUTHORIZATION')
   
    return auth
class MyTokenAuthenticator(BasicAuthentication):
    def authenticate(self, request):
        """
        Returns a `User` if a correct username and password have been supplied
        using HTTP Basic authentication.  Otherwise returns `None`.
        """
        auth = get_my_authorization_header(request)
        
        if request.POST.get('email'):
            return None
        else:
            if auth:
                if auth != request.COOKIES.get('jwt'):
                   
                    msg = _('Invalid Token please login and generate new token')
                    raise exceptions.AuthenticationFailed(msg)
            else:
                msg = _('Please provide token')
                raise exceptions.AuthenticationFailed(msg)

        if not auth or auth[0].lower() != b'basic':
            return None

        if len(auth) == 1:
            msg = _('Invalid basic header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid basic header. Credentials string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            try:
                auth_decoded = base64.b64decode(auth[1]).decode('utf-8')
            except UnicodeDecodeError:
                auth_decoded = base64.b64decode(auth[1]).decode('latin-1')
            auth_parts = auth_decoded.partition(':')
        except (TypeError, UnicodeDecodeError):
            msg = _('Invalid basic header. Credentials not correctly base64 encoded.')
            raise exceptions.AuthenticationFailed(msg)

        userid, password = auth_parts[0], auth_parts[2]
        return self.authenticate_credentials(userid, password, request)

    pass

