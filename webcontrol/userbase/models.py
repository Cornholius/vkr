from django.db import models


class Users(models.Model):

    phone_number = models.CharField(max_length=120, null=False)
    firstname = models.CharField(max_length=120, null=False)
    lastname = models.CharField(max_length=120, null=False)
    entry_counter = models.CharField(max_length=10, null=True)
    start_time = models.CharField(max_length=10, null=True)
    end_time = models.CharField(max_length=10, null=True)
