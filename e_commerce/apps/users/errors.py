from rest_framework import serializers


class PasswordsNotMatchedError(serializers.ValidationError):
    default_detail = "'password' attribute should be euqal to 'password2'"


class PasswordConjugateIsMissing(serializers.ValidationError):
    default_detail = ("'password' and 'password2'"
                        " should be equal to each other")