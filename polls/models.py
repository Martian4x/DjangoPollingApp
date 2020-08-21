import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):  # for your own convenience when dealing with the interactive prompt
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# For more information on model relations, see Accessing related objects. For more on how to use double underscores to perform field lookups via the API, see Field lookups.
# For full details on the database API, see our Database API reference.
# https://docs.djangoproject.com/en/3.0/ref/models/relations/
# https://docs.djangoproject.com/en/3.0/topics/db/queries/#field-lookups-intro
# https://docs.djangoproject.com/en/3.0/topics/db/queries/
