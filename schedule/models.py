from django.db import models
from django.contrib.auth.models import User

day_choices = (
    ('Monday', 'Mon'),
    ('Tuesday', 'Tues'),
    ('Wednesday', 'Wed'),
    ('Thursday', 'Thurs'),
    ('Friday', 'Fri'),
    ('Saturday', 'Sat'),
    ('Sunday', 'Sun'),
)
# Create your models here.
class Choices(models.Model):
    day = models.CharField(max_length=9, choices=day_choices)
    block_start = models.IntegerField(default=0)
    block_length = models.IntegerField(default=1)
    #user = models.ForeignKey(User)

