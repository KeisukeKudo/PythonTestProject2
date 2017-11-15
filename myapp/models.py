from django.db import models


class MessageBord(models.Model):
    new_message = models.TextField(null=False)
