from django.urls import path

from user.views import CustomLoginView, RegisterView, ProfileView, CustomLogoutView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]