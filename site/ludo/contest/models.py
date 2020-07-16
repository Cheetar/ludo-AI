from django.db import models
from main.models import Code
from random import sample

'''
class game():
    players
    history
    result
'''

class Participant(Code):
    father_id = models.IntegerField()
    no_played_games = models.IntegerField(default=0)
    local_rating = models.FloatField(default=1200.)
    score = models.FloatField(default=0.) #

    '''
    def no_played_games_add_1(self): self.no_played_games+=1
    def change_local_rating(self, change): self.local_rating+=change
    def change_score(self, change): self.score+=change
    '''

class Contest(models.Model):
    title = models.CharField(max_length=200)
    participants = models.ManyToManyField(Participant)
    ranking_game = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def choose_players(self):
        no_players = 4
        participants = self.participants.all()
        if len(participants) < no_players: return None
        else:
            players = []
            rand = sample(range(len(participants)), no_players)
            for i in range(no_players):
                players.append(participants[rand[i]])

            return players

    def play(players):
        return 1;

    def update_score():
        pass





    #def add_participant(self, p: Participant): self.participants.add(p)
