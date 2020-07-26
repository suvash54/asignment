from __future__ import unicode_literals
from django.db import models
# Create your models here.
class user_data(models.Model):
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=30)
    #code = models.IntegerField()
    #enter_code = models.IntegerField()
    score = models.IntegerField(default=1)

    '''class meta:
        db_table = "userdata"'''

    def __str__(self):
        return self.user_name

class question(models.Model):
    questions = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    corect = models.CharField(max_length=100)


    def __str__(self):
        return self.questions

class imdb_data(models.Model):
    movieTitle = models.CharField(max_length=50)
    movieDate = models.CharField(max_length=50)
    movieRunTime = models.IntegerField()
    movieGenre = models.CharField(max_length=50)
    moviecerti = models.CharField(max_length=50)
    moviemetascore = models.IntegerField()
    movieDirector = models.CharField(max_length=50)
    def __str__(self):
        return self.movieTitle






