from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator

from bingo_master.validators import DuplicateValidator


class BingoBoard(models.Model):
    start_date = models.DateTimeField("game start datetime")
    end_date = models.DateTimeField("game end datetime")
    board = ArrayField(models.PositiveSmallIntegerField(validators=[MaxValueValidator(75)]),
                       size=75, validators=[DuplicateValidator()])
