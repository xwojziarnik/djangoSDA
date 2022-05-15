from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from users.forms import SignUpForm


class SignUpView(CreateView):
    template_name = 'sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

class UserLoginView(LoginView):
    template_name = 'login.html'

class UserListView(LoginRequiredMixin, ListView):
    template_name = 'user_list.html'
    model = User
