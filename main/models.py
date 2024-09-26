import uuid
from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)  # Store the image URL

    def __str__(self):
        return self.product
