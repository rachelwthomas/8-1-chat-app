from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.urls import reverse_lazy

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

class RoomDeleteView(generic.DeleteView):
    model = Room
    success_url = reverse_lazy('chat_app:chat_rooms')

class MessageDeleteView(generic.DeleteView):
    model = Message
    # success_url = reverse_lazy('chat_app/chat_room_detail.html')

    def delete(self, request, *args, **kwargs):
        # selecting the comment
        self.object = self.get_object()
        # looking up the id to pass to the redirect, looking for the room it is associated with
        room_id = self.object.room.id
        #deleting the commnet
        self.object.delete()
        #once you are done deleting, redirects you to this page.
        return HttpResponseRedirect(reverse_lazy('chat_app:chat_detail', kwargs={'pk': room_id}))

class RoomUpdateView(generic.UpdateView):
    model = Room
    template_name = 'chat_app/create_chat_room_form.html'
    fields = ['name', 'description']
