import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class WhatsApp:

    @staticmethod
    def whats_app(code):
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_ = os.getenv("TWILIO_FROM")
        to = os.getenv("TWILIO_TO")

        client = Client(account_sid, auth_token)

        client.messages.create(
            body=f"Seu código de ativação é: {code}",
            from_=from_,
            to=to
        )