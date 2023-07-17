from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.conf import settings
from django_background_tasks import background
from authentication.models import SavedCurrencyPair


class Command(BaseCommand):
    help = 'Monitor user-saved currency pairs and send email notifications'

    def handle(self, *args, **options):
        # Schedule the background task to run every 5 minutes
        self.schedule_monitor_currency_pairs()


    @background(schedule=5 * 60)  # Run every 5 minutes
    def schedule_monitor_currency_pairs(self):

        # Define the email content
        subject = 'Currency Price Update'
        message_template = '''
        Dear {user},

        We wanted to inform you that there has been a price change in one of your saved currency pairs. Here are the details:

        Currency Pair: {currency_pair}
        Previous Price: {previous_price}
        Current Price: {current_price}
        Change Amount: {change_amount}

        If the change amount exceeds your specified threshold, you will receive this email notification.

        Monitoring Time: {monitoring_time}

        Thank you for using our currency monitoring service.

        Best regards,
        {company}
        '''

        # Set the email parameters
        from_email = settings.EMAIL_HOST_USER  # Retrieve from settings.py
        # Fetch the user-saved currency pairs and iterate over them
        saved_pairs = SavedCurrencyPair.objects.all()
        for pair in saved_pairs:
            # Retrieve the previous price for the currency pair
            previous_price = pair.previous_price
            current_price = 0
            # Calculate the change amount
            change_amount = current_price - previous_price
            # Check if the change amount exceeds the threshold (set your desired threshold)
            if change_amount > 0:
                # Format the message for the recipient
                message = message_template.format(
                    user=pair.user.username,
                    currency_pair=pair.pair,
                    previous_price=previous_price,
                    current_price=current_price,
                    change_amount=change_amount,
                    monitoring_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    company='Your Company Name',
                )
                # Send the email
                send_mail(subject, message, from_email, [pair.user.email])
                self.stdout.write(self.style.SUCCESS(f'Email notification sent to {pair.user.username}'))
