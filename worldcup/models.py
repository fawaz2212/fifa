from django.db import models
from django.shortcuts import render

class Team(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=10)
    coach = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='flags/')

    # Standings fields
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)

    goals_for = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)

    goal_difference = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    jersey_number = models.IntegerField()
    goals = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='players/')


    def __str__(self):
        return self.name


class Stadium(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)

    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    date = models.DateTimeField()

    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)

    status = models.CharField(max_length=20)  # Live, Finished, Upcoming

    def __str__(self):
        return f"{self.team1} vs {self.team2}"


class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Highlight(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    youtube_id = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Knockout(models.Model):
    STAGE_CHOICES = (
        ('R16', 'Round of 16'),
        ('QF', 'Quarter Final'),
        ('SF', 'Semi Final'),
        ('F', 'Final'),
    )

    stage = models.CharField(
        max_length=10,
        choices=STAGE_CHOICES
    )

    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)


    home_logo = models.ImageField( upload_to='teams/', blank=True, null=True )
    away_logo = models.ImageField( upload_to='teams/', blank=True, null=True )

    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)

    match_date = models.DateTimeField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"

class TopScorer(models.Model):
    player_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='scorers/', blank=True, null=True)

    def __str__(self):
        return self.player_name
    



