from django.db import models


class Todo(models.Model):
    TITLE_MAX_LEN = 50

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        ordering = ['-created_at']
