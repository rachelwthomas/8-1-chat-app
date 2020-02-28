from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from .models import Profile

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
    model = Profile
    success_url = reverse_lazy('chat_app:chat_rooms')
    fields = ['location', 'avatar']
    template_name = 'profile_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'profile_detail.html'
