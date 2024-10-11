import celery
import logging

from celery.schedules import crontab


app = celery.Celery('tasks', broker='redis://redis:6379/0')


app.conf.update(
    task_routes = {
        'app.tasks.celery_tasks.store_news_last_hour': {'queue': 'celery'},
        'app.tasks.celery_tasks.store_news_last_day': {'queue': 'celery'}
    },
    broker_connection_retry_on_startup=True,
    result_backend='redis://redis:6379/0',
    beat_schedule={
        'store_news_last_hour': {
            'task': 'app.tasks.celery_tasks.store_news_last_hour',
            'schedule': crontab(minute='*')
        },
        'store_news_last_day': {
            'task': 'app.tasks.celery_tasks.store_news_last_day',
            'schedule': crontab(minute='*')
        }
    },
    timezone='Europe/Moscow'
)


@app.task
def store_news_last_hour():
    from app.scripts.store_news_last_hour import store_news_last_hour
    logging.info("store_news_last_hour task started.")
    store_news_last_hour()
    logging.info("store_news_last_hour task finished.")


@app.task
def store_news_last_day():
    from app.scripts.store_news_last_day import store_news_last_day
    logging.info("store_news_last_day task started.")
    store_news_last_day()
    logging.info("store_news_last_day task finished.")