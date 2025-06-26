from django.contrib.auth.models import AbstractUser
from django.db import models
from django_jalali.db import models as jmodels

from boardgame.models import BoardGame


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=400)
    birthdate = jmodels.jDateField(null=True, blank=True)
    postcode = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.username

class GameMaster(models.Model):
    start_date = jmodels.jDateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class GameMasterKnowledge(models.Model):
    gamemaster = models.ForeignKey(GameMaster, on_delete=models.CASCADE)
    boardgame = models.ForeignKey(BoardGame, on_delete=models.CASCADE)


class ScoreBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.PositiveSmallIntegerField()
    boardgame = models.ForeignKey(BoardGame, on_delete=CASCADE)
    score = models.PositiveSmallIntegerField()