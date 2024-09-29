from django.urls import path

from app import views
from app.views import search_songs, CreateCategoryView, DeleteCategoryView, CreateSingerView, DeleteSingerView, \
    DeleteSongView, UpdateSongView
from app.views import HomeView, CategorySongsView, PlaylistsView,AddToPlaylistView

urlpatterns=[
    path('home/',HomeView.as_view(), name='home'),
    path('category-songs/<int:pk>/',CategorySongsView.as_view(), name='category-songs'),
    path('playlists/',PlaylistsView.as_view(), name='playlists'),
    path('playlist/<int:playlist_id>/add-song/<int:song_id>/', AddToPlaylistView.as_view(), name='add-to-playlist'),
    path('search/', search_songs, name='search_songs'),
    path('playlist/<int:playlist_id>/remove-song/<int:song_id>/', views.remove_song_from_playlist,
         name='remove-song-from-playlist'),
    path('add-category/',CreateCategoryView.as_view(), name='add-category'),
path('delete-category/<int:pk>/', DeleteCategoryView.as_view(), name='delete-category'),
    path('add-singer/', CreateSingerView.as_view(), name='add-singer'),
    path('delete-singer/<int:pk>/', DeleteSingerView.as_view(), name='delete-singer'),
    path('add-song/', views.CreateSongView.as_view(), name='add-song'),
    path('delete-song/<int:pk>/', DeleteSongView.as_view(), name='delete-song'),
    path('edit-song/<int:pk>/', UpdateSongView.as_view(), name='edit-song'),
    path('edit-singer/<int:pk>/', views.UpdateSingerView.as_view(), name='edit-singer'),
    path('edit-category/<int:pk>/', views.UpdateCategoryView.as_view(), name='edit-category'),
    ]