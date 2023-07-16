from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from datetime import datetime


class Command(BaseCommand):
    help = 'Monitor user-saved currency pairs and send email notifications'

    def handle(self, *args, **options):
        # Implement the logic for monitoring currency pairs and sending email notifications

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
        recipient_email = 'ayekhantkhantpo@gmail.com'  # Replace with the recipient's email address

        # Format the message for the recipient
        message = message_template.format(
            user='[User]',
            currency_pair='[Currency Pair]',
            previous_price='[Previous Price]',
            current_price='[Current Price]',
            change_amount='[Change Amount]',
            monitoring_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            company='Sinwattana Crowdfunding Corporation Limited'
        )

        # Send the email
        send_mail(subject, message, from_email, [recipient_email])
        self.stdout.write(self.style.SUCCESS('Email notifications sent'))

