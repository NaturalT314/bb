from django.urls import path

from . import views

urlpatterns = [
    path("frames", views.FrameView.as_view(), name="frame"),
    path("lenses", views.LensView.as_view(), name="lens"),
]