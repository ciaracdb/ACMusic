from django.db import models

class Song(models.Model):
    url = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200, default='')
    player = models.CharField(max_length=200, default='')

class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='')
    url = models.CharField(max_length=200, default='')
    songs = models.ManyToManyField(Song)
    votes = models.IntegerField(default=0)
