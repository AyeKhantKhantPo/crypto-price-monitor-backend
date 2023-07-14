from django.contrib import admin
from .models import AccessLog, SavedCurrencyPair

admin.site.register(AccessLog)
admin.site.register(SavedCurrencyPair)
