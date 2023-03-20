from hashlib import md5

from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    """
    Django ORM model to represent 'members' table.
    """

    email = models.EmailField()

    @property
    def avatar_url(self):
        avatar_hash = md5(self.email.encode()).hexdigest()
        return f'https://www.gravatar.com/avatar/{avatar_hash}?d=mp'
