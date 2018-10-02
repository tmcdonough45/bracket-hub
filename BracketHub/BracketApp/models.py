from django.db import models
# from django_pandas.managers import DataFrameManager
from datetime import datetime

#Superuser information
#User: Tom
#Email: test@gmail.com
#Password: ayaev6969

# Create your models here.
class Show(models.Model):
    name = models.CharField(max_length=69,default='Survivor')

    def __str__(self):
        return self.name

class Season(models.Model):
    show = models.ForeignKey(Show, default=69, on_delete=models.PROTECT)
    subtitle = models.CharField(max_length=69,default='David vs Goliath')
    #premiere = models.DateField(default = datetime.now())

    def __str__(self):
        return "%s: %s" % (self.show, self.subtitle)

class Player(models.Model):
    name = models.CharField(max_length=69,default='John Snow')
    # first_name = models.CharField(max_length=69,default='John')
    # last_name = models.CharField(max_length=69,default='Snow')

    def __str__(self):
        return self.name
        # return "%s %s" % (self.first_name, self.last_name)

class Contestant(models.Model):
    season = models.ForeignKey(Season,default=69,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=69,default='John')
    last_name = models.CharField(max_length=69,default='Snow')
    shameful_exit = models.BooleanField(default=False)
    actual_elimination = models.PositiveIntegerField(default=69)
    num_confessionals = models.PositiveIntegerField(default=0)
    num_individual_immunity_wins = models.PositiveIntegerField(default=0)
    num_votes_against = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

#     objects = DataFrameManager()

class Bracket(models.Model):
    season = models.ForeignKey(Season, default=69, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    contestant = models.ForeignKey(Contestant, on_delete=models.PROTECT)
    predicted_elimination = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s, %s, %s" % (self.player, self.contestant, self.predicted_elimination)

#     objects = DataFrameManager()

class Score(models.Model):
    player = models.CharField(max_length=69,default='John Snow')
    elimination = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    cum_score = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)
    points_back = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s, %s, %s, %s" % (self.player, self.elimination, self.score, self.cum_score)

class Bonus(models.Model):
    season = models.ForeignKey(Season, default=69, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    most_confessionals = models.ForeignKey(Contestant, related_name='q1', on_delete=models.PROTECT)
    most_individual_immunity_wins = models.ForeignKey(Contestant, related_name='q2', on_delete=models.PROTECT)
    most_votes_against = models.ForeignKey(Contestant, related_name='q3', on_delete=models.PROTECT)

    def __str__(self):
        return "%s, %s" % (self.season,self.player)
