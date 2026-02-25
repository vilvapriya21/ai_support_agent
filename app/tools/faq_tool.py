class FAQTool:

    def __init__(self):
        self.faq = {
            "what are your working hours": "We operate from 9 AM to 6 PM.",
            "how to reset password": "Click on 'Forgot Password' at login."
        }

    def lookup(self, message: str):
        return self.faq.get(message.lower())
