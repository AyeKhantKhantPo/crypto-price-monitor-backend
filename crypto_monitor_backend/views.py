import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AccessLog, SavedCurrencyPair
from django.contrib.auth import get_user_model

User = get_user_model()

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

class LogAccessView(APIView):
    def post(self, request, format=None):
        access_log = AccessLog()
        access_log.ip_address = get_client_ip(request)
        access_log.country = get_country_from_ip(access_log.ip_address)
        access_log.time = timezone.now()
        access_log.browser = request.META.get('HTTP_USER_AGENT', '')
        access_log.save()

        return HttpResponse("Access logged successfully")

class NotifyPriceChangeView(APIView):
    def post(self, request, format=None):
        saved_pairs = SavedCurrencyPair.objects.all()

        for pair in saved_pairs:
            pass
            # Check for price changes and send notifications
            # ...

        return HttpResponse('Price change notifications sent')

class SaveCurrencyPairView(APIView):
    def get(self, request, username, format=None):
        try:
            user = User.objects.get(username=username)
            saved_pairs = user.saved_currency_pairs.values_list('pair', flat=True)
            return Response({'savedPairs': list(saved_pairs)}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        # Get the username and currency pair from the request data
        username = request.data.get('username')
        currency_pair = request.data.get('pair')  # Updated field name

        if not currency_pair:
            return Response({'message': 'Currency pair is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Find the user with the given username
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            # Save the currency pair for the user
            saved_pair, created = SavedCurrencyPair.objects.get_or_create(pair=currency_pair)
            user.saved_currency_pairs.add(saved_pair)
            user.save()

            return Response({'message': 'Currency pair saved'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
