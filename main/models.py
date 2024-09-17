import uuid
from django.db import models

class MoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=200)
    kelas = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5