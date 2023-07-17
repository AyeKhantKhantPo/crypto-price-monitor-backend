from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class AccessLog(models.Model):
    country = models.CharField(max_length=255, null=True, blank=True)
    time = models.DateTimeField(default=datetime.now)
    ip_address = models.GenericIPAddressField(default='127.0.0.1')
    browser = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.time:
            self.time = timezone.now()
        super().save(*args, **kwargs)

class SavedCurrencyPair(models.Model):
    pair = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='saved_currency_pairs')
