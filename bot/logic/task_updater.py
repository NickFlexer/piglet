import logging
import json

import requests

from bot.utils import config


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
        else:
            logger.error("response status code " + response.status_code)
    except:
        logger.error("Fail to call web service")
