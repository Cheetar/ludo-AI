from django.db import models
from main.models import Code

'''
class Participant(Code):
    father = models.IntegerField()??
    no_played_games = models.IntegerField(default=0)
    local_rating = models.IntegerField(default=1200)
    score = models.IntegerField(default=0)
'''

class Contest(models.Model):
    title = models.CharField(max_length=200)
    participants = models.ManyToManyField(Code)

    #def add_participant(id: int):
    #    participants.append()
