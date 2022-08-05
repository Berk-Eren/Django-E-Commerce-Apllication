from . import errors
from rest_framework import mixins, viewsets


class PasswordValidatorMixin:
    def validate(self, data):
        if ("password" in self.initial_data)\
            ^ ("password2" in self.initial_data):
            raise errors.PasswordConjugateIsMissing()

        if (("password" in self.initial_data)\
                & ("password2" in self.initial_data)):

            if self.initial_data["password"]\
                    != self.initial_data["password2"]:
                raise errors.PasswordsNotMatchedError()

        return data
