from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'website'

class PaymentConfig(AppConfig):
    name = 'payment'
    verbose_name = 'Payment'

    def ready(self):
        # import signal handlers
        import website.signals
