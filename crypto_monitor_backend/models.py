from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from datetime import datetime


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency_pair = models.CharField(max_length=100)
    last_price = models.DecimalField(max_digits=10, decimal_places=2)
    notification_threshold = models.DecimalField(
        max_digits=10, decimal_places=2)
