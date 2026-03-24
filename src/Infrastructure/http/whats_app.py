from twilio.rest import Client

class WhatsApp:

    @staticmethod
    def whats_app(code):

        account_sid = ""
        auth_token = ""

        client = Client(account_sid, auth_token)

        client.messages.create(
            body=f"Seu código de ativação é: {code}",
            from_='whatsapp:+14155238886',
            to='whatsapp:+5511988413657'
        )