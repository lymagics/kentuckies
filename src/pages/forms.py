from django import forms

from rooms.models import Room


class RoomJoinForm(forms.Form):
    """
    Form to join existing room.
    """

    name = forms.CharField(max_length=100)

    def clean_name(self):
        cleaned_data = self.clean()
        name = cleaned_data.get('name')

        room = Room.objects.filter(name=name).first()
        if room is None:
            raise forms.ValidationError('Room does not exist.')
        return name
