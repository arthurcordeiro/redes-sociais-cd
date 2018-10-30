from django.urls import path

from . import views
from django.views.generic import TemplateView
from redes.views import RedesView

urlpatterns = [
    path('', RedesView.as_view()),
]