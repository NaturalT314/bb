from django.urls import path

from . import views

urlpatterns = [
    path("glasses", views.GlassView.as_view(), name="Glasses"),
]