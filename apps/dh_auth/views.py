from django.urls import reverse_lazy
from django.views.generic import RedirectView, DetailView

from braces.views import LoginRequiredMixin
from allauth.account.views import LoginView, SignupView

from apps.dh_auth.forms import *
from apps.dh_auth.models import *


class UserLogin(LoginView):
    template_name = 'dh_auth/login.html'


class UserSignUp(SignupView):
    template_name = 'dh_auth/signup.html'
    form_class = CustomSignupForm


class CurrentPerfilDetail(LoginRequiredMixin, RedirectView):
    pattern_name = 'perfil_detail'

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('perfil_detail', kwargs={'pk': self.request.user.perfil.id})


class PerfilDetail(DetailView):
    template_name = 'dh_auth/perfil.html'
    model = Perfil
