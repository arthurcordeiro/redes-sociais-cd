from django.urls import path

from . import views
from django.views.generic import TemplateView
from redes.views import TwitterView, FacebookView

urlpatterns = [
    path('twitter', TwitterView.as_view(), name="twitter"),
    path('facebook', FacebookView.as_view(), name="facebook"),
    
]