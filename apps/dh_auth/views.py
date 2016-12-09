from allauth.account.views import LoginView, SignupView
from apps.dh_auth.forms import *
from apps.dh_auth.models import *


class UserLogin(LoginView):
    template_name = 'dh_auth/login.html'


class UserSignUp(SignupView):
    template_name = 'dh_auth/signup.html'
    form_class = CustomSignupForm
