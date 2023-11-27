from django.urls import path
from . import views

urlpatterns = [
    path("", views.feedback_index),
    path("entry", views.feedback_entry)
]