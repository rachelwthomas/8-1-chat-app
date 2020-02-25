from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import TemplateView
from django.views import generic

from .models import Room


class IndexView(TemplateView):
    template_name = 'chat_app/index.html'

class ListView(generic.ListView):
    model = Room
    template_name = 'chat_app/chat_rooms.html'

class DetailView(generic.DetailView):
    model = Room
    template_name = 'chat_app/chat_rooms/chat_room_detail'    


# Create your views here.