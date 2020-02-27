from django.urls import path
from . import views

app_name = 'chat_app'

urlpatterns = [
    path('<int:pk>/chat_room_detail/message_edit',views.MessageUpdateView.as_view(), name='message_edit'),
    path('<int:pk>/chat_room_detail/update', views.RoomUpdateView.as_view(), name='room_update'),
    path('<int:pk>/join_room/', views.JoinRoomView.as_view(), name='join_room'),
    path('<int:pk>/chat_room_detail/add/delete', views.MessageDeleteView.as_view(), name='message_delete'),
    path('<int:pk>/chat_room_detail/delete', views.RoomDeleteView.as_view(), name='room_delete'),
    path('<int:pk>/chat_room_detail/add', views.MessageCreateView.as_view(), name="message_create"),
    path('chat_app/create_chat_room_form/', views.RoomCreateView.as_view(), name='create_room'),
    path('<int:pk>/chat_room_detail', views.DetailView.as_view(), name='chat_detail'),
    path('chat_rooms/', views.ListView.as_view(), name='chat_rooms'),
    path('', views.IndexView.as_view(), name='index'),
]
