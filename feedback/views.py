from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy
from .models import Feedback, Topic
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['topic', 'rating', 'good', 'bad', 'ideas']  # Include all fields in the form
    template_name = "feedback/index.html"
    success_url = reverse_lazy('feedback:index')

    def form_valid(self, form):
        topic_name = form.cleaned_data['topic']
        topic, created = Topic.objects.get_or_create(name=topic_name)
        form.instance.topic = topic
        form.instance.creator_user = self.request.user
        return super().form_valid(form)

class TopicCreateView(UserPassesTestMixin, CreateView):
    model = Topic
    fields = ['name']
    template_name = "feedback/create_topic.html"
    success_url = reverse_lazy('feedback:index')

    def test_func(self):
        return self.request.user.groups.filter(name='topic_masters').exists()
