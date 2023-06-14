from django.db import models
from datetime import date
from django.conf import settings
# Create your models here.

# Projekt Model


class Project(models.Model):
    # owner und permissions erst später dazubauen?
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                           related_name='Projects', on_delete=models.CASCADE)

    project_name = models.CharField(max_length=400)
    project_description = models.TextField(null=True, blank=True)
    project_deadline = models.DateField()
    project_startdate = models.DateField(default=date.today)

    def __str__(self):
        return self.project_name

# Phase Model


class Phase(models.Model):
    phase_name = models.CharField(max_length=400)
    phase_description = models.TextField(null=True, blank=True)
    phase_further_reading = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.phase_name

# To Do Model


class To_Do(models.Model):
    # owner und permissions erst später dazubauen?
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                           related_name='Projects', on_delete=models.CASCADE)
    to_do_name = models.CharField(max_length=400)
    to_do_description = models.TextField()
    to_do_is_done = models.BooleanField(default=False)
    to_do_phase = models.ForeignKey(
        Phase, related_name='To_Dos', on_delete=models.CASCADE)
    to_do_project = models.ForeignKey(
        Project, related_name='To_Dos', on_delete=models.CASCADE)

    def __str__(self):
        return self.to_do_name


class Reward(models.Model):
    # owner und permissions erst später dazubauen?
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                           related_name='rewards', on_delete=models.CASCADE)
    reward_name = models.CharField(max_length=300)
    reward_description = models.TextField()
    reward_picture = models.ImageField(
        null=True, blank=True, upload_to='images/')
    reward_phase = models.ForeignKey(
        Phase, related_name='rewards', on_delete=models.CASCADE)

    def __str__(self):
        return self.reward_name
