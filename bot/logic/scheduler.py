import logging

from django.conf import settings

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import register_events

from . import task_updater
from bot.utils import config


logger = logging.getLogger("testlogger")


def start():
    scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)

    try:
        scheduler.add_job(
            task_updater.get_current_tasks,
            trigger=CronTrigger.from_crontab(config.get_setting("Scheduler", "cron")), 
            id="get_current_tasks",
            max_instances=1,
            replace_existing=True
        )

        scheduler.start()
    except AttributeError:
        logger.error("Scheduler not started!")
