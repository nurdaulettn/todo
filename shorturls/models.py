from django.db import models
from django.contrib.auth.models import User
import string
import random

class ShortUrl(models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_code()
        super().save(*args, **kwargs)

    def generate_code(self, length=6):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
