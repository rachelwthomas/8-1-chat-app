from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

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

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class MessageCreateView(generic.CreateView):
    model = Message
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.room_id = self.kwargs['pk']
        return super().form_valid(form)

class RoomDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Room
    success_url = reverse_lazy('chat_app:chat_rooms')

    def test_func(self):
        obj = self.get_object()
        return obj.created_by == self.request.user


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

class JoinRoomView(LoginRequiredMixin, generic.UpdateView):
    model = Room
    fields = ('members',)

    def post(self, request, *args, **kwargs):
        room = get_object_or_404(Room, pk=self.kwargs['pk'])
        if request.user in room.members.all():
            room.members.remove(request.user)
        else:
            room.members.add(request.user)
        room.save()
        return HttpResponseRedirect(reverse('chat_app:chat_detail', kwargs={'pk': room.id}))


class RoomUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Room
    template_name = 'chat_app/create_chat_room_form.html'
    fields = ['name', 'description']

    def test_func(self):
        obj = self.get_object()
        return obj.created_by == self.request.user

    # def handle_no_permission(self, *args, **kwargs):
    #     self.object = self.get_object()
    #     room_id = self.object.room.id
    #     return redirect('chat_app:chat_detail', kwargs={'pk': room_id})

    def form_valid(self, request, *args, **kwargs):
        # self.object = self.get_object()
        import pdb; pdb.set_trace()
        # self.object.members.add(self.request.user)
        # self.object.save()
        # return super().post(request, *args, **kwargs)

class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Message
    template_name = 'chat_app/message_edit.html'
    fields = ['text']

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

        
