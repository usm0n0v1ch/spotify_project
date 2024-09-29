from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView, DetailView, DeleteView, CreateView

from app.forms import PlaylistForm, SearchForm
from app.models import Category, Song, Playlist, Singer


# Create your views here.


class HomeView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategorySongsView(DetailView):
    model = Category
    template_name = 'app/category_songs.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = Song.objects.filter(category=self.object)
        context['playlist'] = Playlist.objects.first()
        return context


class PlaylistsView(TemplateView):
    template_name = 'app/playlists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists'] = Playlist.objects.all()
        return context


class AddToPlaylistView(View):
    def get(self, request, playlist_id, song_id):

        playlist = get_object_or_404(Playlist, pk=playlist_id)
        song = get_object_or_404(Song, pk=song_id)

        playlist.songs.add(song)

        return redirect('playlists')


def search_songs(request):
    query = request.GET.get('query', '')
    songs = Song.objects.filter(name__icontains=query)


    playlist = Playlist.objects.filter(user=request.user).first()

    form = SearchForm()

    return render(request, 'app/all_songs.html', {
        'songs': songs,
        'playlist': playlist,
        'form': form,
    })


def remove_song_from_playlist(request, playlist_id, song_id):

    playlist = get_object_or_404(Playlist, id=playlist_id)
    song = get_object_or_404(Song, id=song_id)

    if song in playlist.songs.all():
        playlist.songs.remove(song)
        messages.success(request, f'Песня "{song.name}" успешно удалена из плейлиста "{playlist.name}".')
    else:
        messages.error(request, f'Песня "{song.name}" не найдена в плейлисте "{playlist.name}".')

    return redirect('playlists')


class CreateCategoryView(CreateView):
    model = Category
    template_name = 'app/add_category.html'
    fields = ['name', 'photo']
    success_url = reverse_lazy('add-category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class DeleteCategoryView(DeleteView):
    model = Category
    success_url = reverse_lazy('add-category')


class CreateSingerView(CreateView):
    model = Singer
    template_name = 'app/add_singer.html'
    fields = ['name', 'photo']
    success_url = reverse_lazy('add-singer')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['singers'] = Singer.objects.all()
        return context

class DeleteSingerView(DeleteView):
    model = Singer
    success_url = reverse_lazy('add-singer')



class CreateSongView(CreateView):
    model = Song
    template_name = 'app/add_song.html'
    fields = ['name', 'photo', 'audio', 'singer', 'category']
    success_url = reverse_lazy('add-song')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['singers'] = Singer.objects.all()
        context['categories'] = Category.objects.all()
        context['songs'] = Song.objects.all()
        return context

class DeleteSongView(DeleteView):
    model = Song
    success_url = reverse_lazy('add-song')


class UpdateSongView(UpdateView):
    model = Song
    template_name = 'app/edit_song.html'
    fields = ['name', 'photo', 'audio', 'singer', 'category']
    success_url = reverse_lazy('add-song')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['singers'] = Singer.objects.all()
        context['categories'] = Category.objects.all()
        context['songs'] = Song.objects.all()
        return context

class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'app/edit_category.html'
    fields = ['name', 'photo']
    success_url = reverse_lazy('add-category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class UpdateSingerView(UpdateView):
    model = Singer
    template_name = 'app/edit_singer.html'
    fields = ['name', 'photo']
    success_url = reverse_lazy('add-singer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['singers'] = Singer.objects.all()
        return context