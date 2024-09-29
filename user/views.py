from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('home')  # Use reverse_lazy here instead of redirect
        else:
            return reverse_lazy('home')  # Same here


class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')  # Use reverse_lazy for URL resolution

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        if user.is_staff:
            return redirect('home')
        else:
            return redirect('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Use reverse_lazy for URL resolution


class ProfileView(TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(username=self.request.user)
        return context