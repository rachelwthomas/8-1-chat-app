from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/', views.ProfileCreateView.as_view(), name='profile_create'),
    path('signup/', views.SignUpView.as_view(), name='signup')
]
