from django.db import models

# Create your models here.


class MainInfo(models.Model):
    paragraph = models.TextField(blank=False)
    new_paragraph = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

class RecksonInfo(models.Model):
    nickname = models.CharField(max_length=10)
    name = models.CharField(max_length=55)
    bio = models.TextField(blank=True)
    vk_link = models.URLField(blank=True)
    tg_link = models.URLField(blank=True)

    def __str__(self):
        return self.nickname


class AcidInfo(models.Model):
    nickname = models.CharField(max_length=10)
    name = models.CharField(max_length=55)
    bio = models.TextField(blank=True)
    vk_link = models.URLField(blank=True)
    tg_link = models.URLField(blank=True)

    def __str__(self):
        return self.nickname


class HR_contacts(models.Model):
    name = models.CharField(max_length=55)
    company = models.CharField(max_length=255)
    url = models.URLField(blank=False)


class Gameprogress(models.Model):
    name = models.CharField(max_length=3)
    score = models.IntegerField()
    game_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


