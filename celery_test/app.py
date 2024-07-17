import datetime

from celery import Celery

BROKER_URL = "redis://127.0.0.1:6379/0"
BACKEND_URL = "redis://127.0.0.1:6379/0"
ONCE_REDIS_URL = "redis://127.0.0.1:6379/0"


app = Celery("celery_test.tasks", set_as_current=False)

CELERY_CONFIG = dict(
    imports=[
        # importing this will also load the tasks, so that the application registers them
        # NOTE: If a celery worker receives a task that is not known, it will discard it and it will be lost.
        # Make sure to load all the tasks definition in all the celery workers.
        "celery_test.tasks",
    ],
    task_routes={
        "celery_test.tasks.*": {"queue": "tasks"},
    },
    broker_url=BROKER_URL,
    result_backend=BACKEND_URL,
    accept_content=("json", "pickle"),
    task_serializer="pickle",
    task_time_limit=600,  # Limit tasks to 10 minutes (600 seconds)
    result_serializer="pickle",
    ONCE=dict(
        backend="celery_once.backends.Redis",
        settings=dict(
            url=ONCE_REDIS_URL,
            default_timeout=int(datetime.timedelta(hours=1).total_seconds()),
        ),
    ),
    broker_transport_options={
        "queue_order_strategy": "priority",
        "priority_steps": list(range(10)),
        "sep": ":",
    }
)

app.config_from_object(CELERY_CONFIG)