import asyncio
import celery

from celery.schedules import crontab


app = celery.Celery('tasks', broker='redis://localhost:6379/0')


app.conf.update(
    task_routes={
        'app.tasks.database_tasks.*': {'queue': 'database_tasks_queue'}
    },
    broker_connection_retry_on_startup=True,
    result_backend='redis://localhost:6379/0',
    beat_schedule={
        'get_news_last_hour': {
            'task': 'app.tasks.celery.store_news_last_hour',
            'schedule': crontab(minute=1, hour=0)
        }
    },
    timezone='Europe/Moscow'
)


@app.task
def store_news_last_hour():
    from app.redis.store_news_last_hour import store_news_last_hour
    asyncio.run(store_news_last_hour())