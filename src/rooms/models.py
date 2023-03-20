from django.db import models
from django.conf import settings
from django.urls import reverse


class Room(models.Model):
    """
    Django ORM model for 'rooms' table.
    """

    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rooms')

    def join(self, member):
        """
        Join room.
        """

        self.members.add(member)
        self.save()

    def leave(self, member):
        """
        Leave room.
        """

        self.members.remove(member)
        self.save()

    def is_member(self, member):
        """
        Check if user is room member.
        """

        return member in self.members.all()

    def get_absolute_url(self):
        return reverse('rooms:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
