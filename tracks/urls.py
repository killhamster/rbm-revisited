from django.urls import path
from . import views

urlpatterns = [
    path("", views.track_index, name="track_index"),
    path("<int:pk>/", views.track_detail, name="track_detail"),
]
