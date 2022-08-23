from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class RedisCacheMixin:
    @method_decorator(cache_page(settings.CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)