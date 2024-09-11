from django.db import models

class MoodEntry(models.Model):
    nama = models.CharField(max_length=200)
    kelas = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5