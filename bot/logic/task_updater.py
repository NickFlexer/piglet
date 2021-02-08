import logging
import json
import datetime

import requests

from bot.utils import config
from bot.models import Task


logger = logging.getLogger("testlogger")


def get_current_tasks():
    url = config.get_setting("Yandex", "url")
    headers = {
        "Authorization" : "OAuth " + config.get_setting("Yandex", "token"),
        "X-Org-ID" : config.get_setting("Yandex", "org"),
        "Content-Type": "application/json"
    }
    body = config.get_setting("Yandex", "json-body")

    try:
        response = requests.request("POST", url=url, headers=headers, data=body)

        if response.status_code == 200:
            logger.info("Response body: " + response.text)
            result = json.loads(response.text)

            if not is_task_exist(result) and len(result) > 0:
                save_task(result)
        else:
            logger.error("response status code " + response.status_code)
    except:
        logger.error("Fail to call web service")


def is_task_exist(body):
    try:
        res = Task.objects.get(key=body["key"])
        return True
    except Entry.DoesNotExist:
        return False


def save_task(body):
    task = Task()
    task.key = body["key"]
    task.summary = body["summary"]
    task.created_at = datetime.datetime.strptime(body["createdAt"], "%Y-%m-%dT%H:%M:%S.%f%z")
    task.save()
