from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy
from .models import Feedback, Topic
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
class FeedbackCreateView(CreateView):
    model = Feedback

    # Include all fields except creator_user in the form
    # creator_user is set automatically in the form_valid() method
    fields = ['topic', 'rating', 'good', 'bad', 'ideas']
    template_name = "feedback/index.html"
    success_url = reverse_lazy('feedback:index')

    # CreateView has a get_context_data() method that creates a context variable
    # which contains data about the form and the current view.
    # get_context_data() is automatically called when the view is rendering the template.
    # We're overriding it here to add a variable that indicates whether the current user
    # is a member of the topic_masters group.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['is_topic_master'] = current_user.groups.filter(name='topic_masters').exists()

        return context

    # This is called automatically when valid form data has been POSTed
    def form_valid(self, form):
        topic_name = form.cleaned_data['topic']
        topic, is_created = Topic.objects.get_or_create(name=topic_name)
        form.instance.topic = topic
        form.instance.creator_user = self.request.user

        # This saves the form instance to the database and redirects to the success_url
        # This is default behavior, but we're overriding it to add the topic and creator_user
        return super().form_valid(form)

class TopicCreateView(UserPassesTestMixin, CreateView):
    model = Topic
    fields = ['name']
    template_name = "feedback/create_topic.html"
    success_url = reverse_lazy('feedback:index')

    def test_func(self):
        return self.request.user.groups.filter(name='topic_masters').exists()
