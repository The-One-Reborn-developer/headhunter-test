from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField()
    password = models.TextField()


class Question(models.Model):
    question = models.CharField(max_length=200)
    right_answer = models.CharField(max_length=200)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)