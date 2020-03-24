from django.db import models

# Create your models here.


class Question(models.Model):
    # creates PK w/ auto increment
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text  # reveal views


class Choice(models.Model):
    # relationships
    # if question is deleted, choices are also deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
