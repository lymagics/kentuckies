from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Member
from .forms import MemberCreationForm, MemberChangeForm


@admin.register(Member)
class MemberAdmin(UserAdmin):
    """
    Django admin model to represent Member model in admin panel.
    """

    model = Member
    form_add = MemberCreationForm
    form = MemberChangeForm
    list_display = ('pk', 'username',)
    list_display_links = ('username',)
