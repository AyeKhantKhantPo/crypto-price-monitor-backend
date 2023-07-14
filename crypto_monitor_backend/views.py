import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .models import AccessLog, SavedCurrencyPair


def get_country_from_ip(ip):
    url = f'http://ip-api.com/json/{ip}'
    response = requests.get(url)
    data = response.json()
    country = data.get('country')
    return country


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@csrf_exempt
def log_access(request):
    access_log = AccessLog()
    access_log.ip_address = get_client_ip(request)
    access_log.country = get_country_from_ip(access_log.ip_address)
    access_log.time = timezone.now()
    access_log.browser = request.META.get('HTTP_USER_AGENT', '')
    access_log.save()

    return HttpResponse("Access logged successfully")


def notify_price_change(request):
    saved_pairs = SavedCurrencyPair.objects.all()

    for pair in saved_pairs:
        pass
        # Check for price changes and send notifications
        # ...

    return HttpResponse('Price change notifications sent')
