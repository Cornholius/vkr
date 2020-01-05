from django.db import models


class Users(models.Model):

    phone_number = models.CharField(max_length=12)
    firstname = models.CharField(max_length=120, blank=True)
    lastname = models.CharField(max_length=120, blank=True)
    entry_counter = models.CharField(max_length=10, blank=True)
    start_time = models.CharField(max_length=10, blank=True)
    end_time = models.CharField(max_length=10, blank=True)
