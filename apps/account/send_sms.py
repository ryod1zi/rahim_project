from django.conf import  settings
from twilio.rest import  Client



def send_activation_sms(phone_number, actvation_code):
    message = f'Ваш код активации: {actvation_code}'
    client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(body=message, from_=settings.TWILIO_SENDER_PHONE,
                           to=phone_number)