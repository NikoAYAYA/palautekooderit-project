from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy
from .models import Feedback

# Create your views here.
class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['topic', 'rating', 'good', 'bad']
    template_name = "feedback/index.html"
    success_url = reverse_lazy('feedback:index')
