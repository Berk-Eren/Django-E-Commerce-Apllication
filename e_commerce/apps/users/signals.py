from django.conf import settings
from django.dispatch import receiver
from django.core.signals import request_finished
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance=None, created=False, **kwargs):
    Token.objects.get_or_create(user=instance)

@receiver(request_finished)
def after_request(sender, *args, **kwargs):
    print("Request was sent")