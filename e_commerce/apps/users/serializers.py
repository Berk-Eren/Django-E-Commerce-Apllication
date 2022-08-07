from rest_framework import serializers

from .models import User
from . import mixins


class UserBaseSerializer(mixins.PasswordValidatorMixin, 
                            serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["full_name", "email", "username", "password", "password2"]
    
    def save(self, *args, **kwargs):
        self.validated_data.pop("password2", None)
    
        return super().save(*args, **kwargs)


class UserDetailCreateSerializer(UserBaseSerializer):
    password = serializers.CharField(write_only=True, required=True,
                                        style={'input_type': 'password'} )
    password2 = serializers.CharField(write_only=True, required=True,
                                        style={'input_type': 'password'} )

    def create(self, validated_data):
        password = self.validated_data.pop("password")

        model = self.Meta.model

        user = model.objects.create(**self.validated_data)
        user.set_password(password)

        return user


class UserUpdateSerializer(UserBaseSerializer):
    password = serializers.CharField(write_only=True, required=False,
                                        style={'input_type': 'password'} )
    password2 = serializers.CharField(write_only=True, required=False,
                                        style={'input_type': 'password'} )

    def update(self, instance, validated_data):
        if (password := self.validated_data.pop("password", None)):
            model = self.Meta.model
            
            user = super().update(instance, validated_data)
            user.set_password(password)
            user.save()

            return user

        return super().update(instance, validated_data)
