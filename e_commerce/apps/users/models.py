from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser as DjangoAbstractUser


class User(DjangoAbstractUser):
    full_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        slug_txt = "{} {}".format(self.username, 
                                    self.full_name)
        self.slug = slugify(slug_txt)
        
        super().save(*args, **kwargs)