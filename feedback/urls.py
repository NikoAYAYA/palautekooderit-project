from django.urls import path
from . import views
from .views import TopicCreateView

app_name = 'feedback'
urlpatterns = [
    path('', views.FeedbackCreateView.as_view(), name='index'),
    path('create-topic/', TopicCreateView.as_view(), name='create_topic'),
    path('results/', views.ResultsView.as_view(), name='results'),
]
