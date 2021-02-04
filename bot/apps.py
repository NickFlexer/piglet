from django.conf import settings

from django.apps import AppConfig


class BotConfig(AppConfig):
    name = 'bot'

    def ready(self):
        from .logic import scheduler
        if settings.SCHEDULER_AUTOSTART:
        	scheduler.start()
