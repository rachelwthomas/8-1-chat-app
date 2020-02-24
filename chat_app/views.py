from django.views.generic.base import TemplateView
from django.views import generic


class IndexView(TemplateView):
    template_name = 'chat_app/index.html'

# Create your views here.
