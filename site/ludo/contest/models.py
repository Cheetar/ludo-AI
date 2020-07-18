from django.db import models
from main.models import Code
from random import sample
from trueskill import Rating, rate, TrueSkill

'''
class game(models.Model):
    players
    history
    result
'''

class Participant(Code):
    father_id = models.IntegerField()
    no_played_games = models.IntegerField(default=0)
    #local_rating = models.FloatField(default=1200.)
    score = models.FloatField(default=0.) #
    #rating = Rating()
    def set_rating(self, rating): self.rating = rating

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

    def play(self, players):
        return 1;

    def update_score(self, players, winner):
        result = [0,0,0,0]
        result[winner] = 1

        players[0].rating, players[1].rating, players[2].rating, players[3].rating = rate([[players[0].rating], [players[1].rating], [players[2].rating], [players[3].rating]])

        for i in range(4):
            players[i].set_rating(players[i].rating)
            players[i].save()
            '''
            p = Participant.objects.get(id=players[i].id)
            p.rating = players[i].rating
            p.save()
            '''

        for i in range(4):
            print(players[i].rating)
            '''
        for i in range(4):
            players[i].save()
        '''
        print('Mecz rozegrany!')
    #def add_participant(self, p: Participant): self.participants.add(p)

    def game(self):
        TrueSkill(backend='mpmath').cdf
        players = self.choose_players()
        if players != None:
            winner = self.play(players)
            #if self.ranking_game:
            self.update_score(players, winner)
