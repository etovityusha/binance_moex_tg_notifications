import os

import requests
from celery import Celery
from celery.schedules import crontab

from checker import ProfitChecker

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
celery.conf.beat_schedule = {
    'run_all_scenarios': {
        'task': 'run_all_scenarios',
        'schedule': crontab(minute="*/1"),
    },
}


@celery.task(name='run_all_scenarios')
def run_all_scenarios():
    scenarios_list = requests.get('http://158.101.192.82:6110/scenarios').json()['scenarios']
    for scenario_id in scenarios_list:
        run_checker.apply_async(kwargs={'scenario_id': scenario_id})


@celery.task(name="run_checker")
def run_checker(scenario_id: int):
    ProfitChecker(scenario_id).run()
