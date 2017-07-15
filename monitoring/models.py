# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    fb_id = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    mailbox = models.CharField(max_length = 100)

class Monitor(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    site_url = models.CharField(max_length = 250)
    frequency = models.IntegerField(max_length = 10)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

class Alert(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete = models.CASCADE)
    action = models.ForeignKey(Action, on_delete = models.CASCADE)
    threshold = models.CharField()
    message = models.CharField(max_length = 500)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

class Action(models.Model):
    command = models.CharField(max_length = 100)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    DOWN = 0
    ACTIVE = 1
    CHECKING = 2
    status = (
        (DOWN, 'Down'),
        (ACTIVE, 'Active'),
        (CHECKING, 'Checking'),
    )

