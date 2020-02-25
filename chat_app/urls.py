from django.urls import path
from . import views

app_name = 'chat_app'

urlpatterns = [
    path('<int:pk>/chat_room_detail', views.DetailView.as_view(), name='chat_detail'),
    path('chat_rooms/', views.ListView.as_view(), name='chat_rooms'),
    path('', views.IndexView.as_view(), name='index'),
]
