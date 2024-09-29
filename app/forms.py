from django import forms
from .models import Playlist

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'songs']  # Укажите поля, которые нужно редактировать


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)