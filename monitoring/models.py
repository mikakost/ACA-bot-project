# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MinValueValidator
from django.db import models


class User(models.Model):
    fb_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mailbox = models.EmailField(max_length=100)

    def __str__(self):
        return "Name = {}, email = {}".format(self.name, self.mailbox)


class Monitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_url = models.URLField(max_length=250)
    frequency = models.IntegerField(default=600, validators=[
            MinValueValidator(0)
        ])
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Action(models.Model):
    command = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    # DOWN = 0
    # ACTIVE = 1
    # CHECKING = 2
    # status = (
    #     (DOWN, 'Down'),
    #     (ACTIVE, 'Active'),
    #     (CHECKING, 'Checking'),
    # )


class Alert(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    threshold = models.FloatField()
    message = models.CharField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
