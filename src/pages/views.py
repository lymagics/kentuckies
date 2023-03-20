from django.views.generic import View, TemplateView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from braces.views import AnonymousRequiredMixin

from .forms import RoomJoinForm
from members.forms import MemberCreationForm
from rooms.models import Room


class HomePageGet(TemplateView):
    """
    Http GET method for home page.
    """

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RoomJoinForm
        return context


class HomePagePost(LoginRequiredMixin, FormView):
    """
    Http POST method for home page.
    """

    form_class = RoomJoinForm
    template_name = 'home.html'

    def form_valid(self, form):
        self.room = Room.objects.get(name=form.cleaned_data['name'])
        return super().form_valid(form)

    def get_success_url(self):
        return self.room.get_absolute_url()


class HomePageView(View):
    """
    Home page view.
    """

    def get(self, request, *args, **kwargs):
        view = HomePageGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = HomePagePost.as_view()
        return view(request, *args, **kwargs)


class LoginPageView(AnonymousRequiredMixin, LoginView):
    """
    Login page view.
    """

    template_name = 'auth/login.html'


class LogoutPageView(LoginRequiredMixin, LogoutView):
    """
    Logout page view.
    """
    pass


class SignUpPageView(AnonymousRequiredMixin, CreateView):
    """
    Register new user.
    """

    form_class = MemberCreationForm
    success_url = reverse_lazy('pages:login')
    template_name = 'auth/signup.html'
