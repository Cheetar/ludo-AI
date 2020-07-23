from django.db import models
from main.models import Code
from random import sample
from trueskill import Rating, rate, TrueSkill

'''
class game(models.Model):
    players_ids
    history
'''

class Participant(Code):
    father_id = models.IntegerField()
    #father = models.ForeignKey(Code, on_delete=models.CASCADE)
    no_played_games = models.IntegerField(default=0)
    score = models.FloatField(default=0.)
    rating = Rating()
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

    def update_score(self, p: list, winner): #p – list which contains 4 participants
        result = [2,2,2,2]
        result[winner] = 1

        for i in range(4):
            print(p[i].rating)

        n0, n1, n2, n3 = rate([[p[0].rating], [p[1].rating], [p[2].rating], [p[3].rating]], ranks=result)
        #p[0].rating, p[1].rating, p[2].rating, p[3].rating
        print(type(n0))
        print(len(n0))
        print(n0[0])
        print(type(n0))
        p[0].rating=n0[0]
        p[0].save()
        p[1].rating=n1[0]
        p[2].rating=n2[0]
        p[3].rating=n3[0]
        p[1].save()
        p[2].save()
        p[3].save()
        p[winner].score+=1

        for i in range(4):
            p[i].no_played_games+=1
            p[i].save()

            q = Participant.objects.get(id=p[i].id)
            q.set_rating(p[i].rating)
            #q.rating = p[i].rating
            q.save()
        for i in range(4):
            print(p[i].rating)
        print('Mecz rozegrany!')
    #def add_participant(self, p: Participant): self.participants.add(p)

    def game(self):
        TrueSkill(backend='mpmath').cdf
        players = self.choose_players()
        if players != None:
            winner = self.play(players)
            if self.ranking_game:
                self.update_score(players, winner)
                for p in self.participants.all():
                    print(p.rating)
