# notes/models.py
from django.db import models
from profiles.models import Ape


class ObservationNote(models.Model):
    ape = models.ForeignKey(Ape, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"Note for {self.ape.name} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"
        )
