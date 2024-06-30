from django.db import models

# Create your models here.
class User(models.Model):

    class Meta:
        db_table = 'user'

    name = models.CharField(blank=False, max_length=50)
    contact = models.CharField(blank=False, max_length=50)
    email = models.CharField(blank=False, max_length=50)
    address = models.CharField(blank=False, max_length=250)
    user_name = models.CharField(blank=False, max_length=25, default=None)
    password = models.CharField(max_length=10, blank=False, default=None)


class History(models.Model):

    class Meta:
        db_table = 'history'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.CharField(blank=False, max_length=50)
    weight = models.CharField(blank=False, max_length=50)
    bmi = models.CharField(blank=False, max_length=50)
    hirsutism = models.CharField(blank=False, max_length=50)
    skin = models.CharField(blank=False, max_length=25, default=None)
    acene = models.CharField(max_length=10, blank=False, default=None)
    menstrual = models.CharField(max_length=10, blank=False, default=None)
    sleep = models.CharField(max_length=10, blank=False, default=None)
    hair = models.CharField(max_length=10, blank=False, default=None)
    result1 = models.CharField(max_length=100, blank=False, default=None)
    result2 = models.CharField(max_length=100, blank=False, default='null')