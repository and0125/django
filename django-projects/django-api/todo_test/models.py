from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)

    def __str__(self):
        return self.title