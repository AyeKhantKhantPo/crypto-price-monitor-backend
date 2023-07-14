from django.db import models
from django.contrib.auth.models import User

class AccessLog(models.Model):
    country = models.CharField(max_length=100)
    time = models.DateTimeField()
    browser = models.CharField(max_length=100)

class SavedCurrencyPair(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency_pair = models.CharField(max_length=100)
    last_price = models.DecimalField(max_digits=10, decimal_places=2)
    notification_threshold = models.DecimalField(max_digits=10, decimal_places=2)
