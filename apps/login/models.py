from __future__ import unicode_literals
from django.db import models
import bcrypt
import re


class Entity(models.Model):
    entity_name = models.CharField(max_length=100)
    state_of_inc = models.CharField(max_length=100)
    date_of_inc = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
