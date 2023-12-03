from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Topic(models.Model):
    creator_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Feedback(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    creator_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    good_feedback = models.TextField()
    bad_feedback = models.TextField()
    improvement_feedback = models.TextField()