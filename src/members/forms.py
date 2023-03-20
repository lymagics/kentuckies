from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Member


class MemberCreationForm(UserCreationForm):
    """
    Member creation form used in admin panel.
    """

    class Meta:
        model = Member
        fields = ('username', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in ('username', 'password1', 'password2'):
            self.fields[field].help_text = None


class MemberChangeForm(UserChangeForm):
    """
    Member change form used in admin panel.
    """

    class Meta:
        model = Member
        fields = ('username', 'email',)
