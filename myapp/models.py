from django.db import models

# Create your models here.
class Team(models.Model):
    teamname = models.CharField(max_length=30)
    teamscore = models.IntegerField(default=0)

    def __str__(self):
    	return self.teamname
