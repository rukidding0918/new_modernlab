from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserSignupForm


class UserSignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserSignupForm
    success_url = reverse_lazy("index")
