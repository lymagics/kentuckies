from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Member


class MemberDetailView(View):
    """
    Get information about existing user.
    """

    def get(self, request, pk, *args, **kwargs):
        member = get_object_or_404(Member, pk=pk)
        return JsonResponse({
            'uid': member.pk,
            'avatar_url': member.avatar_url,
        })
