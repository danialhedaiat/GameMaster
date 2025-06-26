from django.db import models

# Create your models here.

class ComponentTag(models.Model):
    component = models.ForeignKey(BoardGameComponent, on_delete=models.CASCADE, related_name='tags')
    tag = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.tag} for {self.component.name} component"


class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    boardgame = models.ForeignKey(BoardGame, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL)


class BoardGameRanking(models.Model):
    rank = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    boardgame = models.ForeignKey(BoardGame, on_delete=models.SET_NULL)
