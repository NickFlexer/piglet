import logging

from django.conf import settings

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job


from . import task_updater
from bot.utils import config


logger = logging.getLogger("testlogger")


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    
    try:
        scheduler.add_job(
            task_updater.get_current_tasks,
            trigger=CronTrigger.from_crontab(config.get_setting("Scheduler", "cron")), 
            id="get_current_tasks",
            max_instances=1,
            replace_existing=True
        )

        register_events(scheduler)
        scheduler.start()
    except AttributeError:
        logger.error("Scheduler not started!")
