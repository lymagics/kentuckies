from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from .models import Room
from .utils import generate_agora_token


class RoomCreateView(LoginRequiredMixin, CreateView):
    """
    Create new room.
    """

    model = Room
    fields = ('name',)
    template_name = 'rooms/new.html'


class RoomDetailView(LoginRequiredMixin, DetailView):
    """
    Join an existing room.
    """

    model = Room
    template_name = 'rooms/detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.is_member(request.user):
            self.object.join(request.user)

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['APP_ID'] = settings.AGORA_APP_ID
        context['TOKEN'] = generate_agora_token(self.request.user.pk, self.object.name)
        context['CHANNEL_NAME'] = self.object.name
        return context
