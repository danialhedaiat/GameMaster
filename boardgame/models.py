from django.db import models

from main.models import User


class BoardGame(models.Model):
    class Category(models.TextChoices):
        STRATEGY = 'ST', 'Strategy'
        FAMILY = 'FA', 'Family'
        PARTY = 'PA', 'Party'
        COOP = 'CO', 'Cooperative'
        CARD = 'CA', 'Card Game'
        WAR = "WA", 'War Game'

    name = models.CharField(max_length=100)
    description = models.TextField()
    play_time = models.TimeField()
    cover_image = models.ImageField(upload_to='BoardGame/')
    category = models.CharField(max_length=2, choices=Category.choices)
    difficulty = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class BoardGameComponent(models.Model):
    class ComponentType(models.TextChoices):
        BOARD = 'BOARD', 'Board'
        CARD = 'CARD', 'Card'
        TILE = 'TILE', 'Tile'
        PAWN = 'PAWN', 'Pawn'
        DICE = 'DICE', 'Dice'
        TOKEN = 'TOKEN', 'Token'
        RULEBOOK = 'RULEBOOK', 'Rulebook'
        OTHER = 'OTHER', 'Other'
    boardgame = models.ForeignKey(BoardGame, related_name='components', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=ComponentType.choices)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='components/', blank=True, null=True)
    score = models.CharField(max_length=20, null=True, blank=True)
    cost_value = models.CharField(max_length=100, null=True, blank=True)
    event = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class ComponentTag(models.Model):
    component = models.ForeignKey(BoardGameComponent, on_delete=models.CASCADE, related_name='tags')
    tag = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.tag} for {self.component.name} component"


class Tutorial(models.Model):
    class TutorialStatus(models.TextChoices):
        DRAFT = 'DR', 'draft'
        PUBLISH = 'PB', 'publish'

    title = models.CharField(max_length=100)
    boardgame = models.ForeignKey(BoardGame, on_delete=models.SET_NULL)
    text = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='tutorial/videos/', null=True, blank=True)
    voice = models.FileField(upload_to='tutorial/voices/', null=True, blank=True)
    status = models.CharField(max_length=2, choices=TutorialStatus.choices)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL)


class BoardGameRanking(models.Model):
    rank = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    boardgame = models.ForeignKey(BoardGame, on_delete=models.SET_NULL)


class BoardGameComment(models.Model):
    bordgame = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    reply = models.ForeignKey('BoardGameComment', on_delete=models.CASCADE, null=True)
    comment = models.TextField()


class ShelfLocation(models.Model):
    boardgame = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    shelf_id = models.PositiveSmallIntegerField()
