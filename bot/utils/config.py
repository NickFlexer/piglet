import logging

from django.conf import settings

from bot.models import Setting


logger = logging.getLogger(__name__)


def get_setting(topic, setting):
    try:
        res = Setting.objects.get(topic=topic, setting=setting)
    except Setting.DoesNotExist:
        res = None

    if not res:
        logger.error("Setting '" + topic + "-" + setting + "' not found!")
        return None
    else:
        return res.value
