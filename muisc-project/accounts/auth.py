from functools import wraps

class AuthenticationDecorator:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            auth_header = kwargs.get('auth_header')

            if not self.authenticate(auth_header):
                raise Exception("401!")

            return func(*args, **kwargs)

        return wrapper

    def authenticate(self, auth_header):
        if auth_header:
            auth_type, auth_token = auth_header.split()
            if auth_type.lower() == 'basic':
                credentials = auth_token.strip().decode('base64').split(':')
                username, password = credentials
                if username == self.username and password == self.password:
                    return True

        return False