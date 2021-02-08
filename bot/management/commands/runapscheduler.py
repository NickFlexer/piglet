import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from bot.utils import config
from bot.logic import task_updater


logger = logging.getLogger("testlogger")


class Command(BaseCommand):
    help = "Run apscheduler"

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        try:
            scheduler.add_job(
                task_updater.get_current_tasks,
                trigger=CronTrigger.from_crontab(config.get_setting("Scheduler", "cron")), 
                id="get_current_tasks",
                max_instances=1,
                replace_existing=True
            )
            logger.info("Added job 'get_current_tasks'")

            try:
                logger.info("Starting scheduler...")
                scheduler.start()
            except KeyboardInterrupt:
                logger.info("Stopping scheduler...")
                scheduler.shutdown()
                logger.info("Scheduler shut down successfully!")
        except AttributeError:
            logger.error("Scheduler not started!")
