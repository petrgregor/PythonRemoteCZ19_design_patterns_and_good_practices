import random


class Credentials:
    def get_credentials(self, user_id):
        pass


class AWSSignature(Credentials):
    def get_credentials(self, user_id):
        return "98f92d42-66c7-4ce4-a834-087a783133e7"


class BearerToken(Credentials):
    def get_credentials(self, user_id):
        return "1/mZ1edKKACtPAb7zGlwSzvs72PvhAbGmB8K1ZrGxpcNM"


class UserNameAndPasswordCredentials(Credentials):
    def get_credentials(self, user_id):
        return "andrew:Andrew_123"


class AuthenticationHandler:
    def authenticate(self, credentials):
        pass

    def supports(self, cls):
        pass


class AWSAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.authenticate_in_aws(credentials)
        else:
            return False

    def supports(self, cls):
        return isinstance(cls, AWSSignature)

    def authenticate_in_aws(self, credentials):
        return random.randint(1, 3) == 1


class BearerTokenAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.is_token_valid(credentials)
        else:
            return False

    def supports(self, cls):
        return isinstance(cls, BearerToken)

    def is_token_valid(self, credentials):
        return random.randint(1, 3) == 2


class UserNameAndPasswordAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.is_password_valid(credentials)
        else:
            return False

    def supports(self, cls):
        return isinstance(cls, UserNameAndPasswordCredentials)

    def is_password_valid(self, credentials):
        return random.randint(1, 3) == 3


class ChainAuthenticationElement:
    def __init__(self, authentication_handler, next=None):
        self._authentication_handler = authentication_handler
        self._next = next

    def authenticate(self, credentials):
        if self._authentication_handler.authenticate(credentials):
            print(f"Authentication using handler {credentials.__class__.__name__}")
            return True
        else:
            return self._next and self._next.authenticate(credentials)


def main():
    authentication_handler_unp = UserNameAndPasswordAuthenticationHandler()
    authentication_handler_bearer = BearerTokenAuthenticationHandler()
    authentication_handler_aws = AWSAuthenticationHandler()

    last_element = ChainAuthenticationElement(authentication_handler_aws)
    middle_element = ChainAuthenticationElement(authentication_handler_bearer, last_element)
    first_element = ChainAuthenticationElement(authentication_handler_unp, middle_element)

    first_element.authenticate(AWSSignature())
    first_element.authenticate(UserNameAndPasswordCredentials())
    first_element.authenticate(BearerToken())


if __name__ == '__main__':
    main()
