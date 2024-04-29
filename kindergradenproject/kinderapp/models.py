from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class values(models.Model):
    numberss = models.CharField(max_length=25)
    valuess = models.CharField(max_length=25)
    g = models.IntegerField()

class CustomUser(AbstractUser):
    is_contributer = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)

class Postupload(models.Model):
    yourprimarykeyfield = models.AutoField(primary_key=True)
    video = models.FileField(upload_to='videos/',blank=True, null=True, default=None)
    audio = models.FileField(upload_to='audio/',blank=True, null=True, default=None)
    image = models.ImageField(upload_to='images/',blank=True, null=True, default=None)
    uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pv = models.ForeignKey(values, on_delete=models.CASCADE)
    vari = models.CharField(max_length=100, default='NOT VARIFIED')
    is_seen = models.CharField(max_length=100, default='not_seen')
    color = models.CharField(max_length=100,default="#FA7070")


# class Suggestion(models.Model):
#     post = models.ForeignKey(id, on_delete=models.CASCADE)
#     suggestion =  models.CharField(max_length=100, null=True, blank=True)


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Postupload, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comments=models.CharField(max_length=100,null=True, blank=True, default=None)


class saw(models.Model):
    pos = models.ForeignKey(Postupload, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    isseen = models.CharField(max_length=100, default='not_seen')
    colors = models.CharField(max_length=100, default="#FA7070")
