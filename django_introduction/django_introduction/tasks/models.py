from django.db import models


class Tasks(models.Model):
    title = models.CharField(
        max_length=50,
        null=False,
        # unique=True,
    )

    text = models.TextField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'Task: {self.title}, {self.text}'


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'Category: {self.name}'
