from django.db import models

class Item(object):
    text = models.TextField(default='')