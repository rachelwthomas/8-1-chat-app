from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import TemplateView
from django.views import generic
from django.urls import reverse

from .models import Room, Message


class IndexView(TemplateView):
    template_name = 'chat_app/index.html'

class ListView(generic.ListView):
    model = Room
    template_name = 'chat_app/chat_rooms.html'

class DetailView(generic.DetailView):
    model = Room
    template_name = 'chat_app/chat_room_detail.html'
    fields = ['name']

class RoomCreateView(generic.CreateView):
    model = Room
    template_name = 'chat_app/create_chat_room_form.html'
    fields = ['name', 'description']

class MessageCreateView(generic.CreateView):
    model = Message
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.room_id = self.kwargs['pk']
        return super().form_valid(form)
