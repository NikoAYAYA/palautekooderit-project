from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=160)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[
        MinValueValidator(1), MaxValueValidator(5)])
    good = models.TextField(max_length=2000, blank=True)
    bad = models.TextField(max_length=2000, blank=True)
    ideas = models.TextField(max_length=2000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    creator_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"
