import time

from celery_test.app import app


@app.task()
def one_tenth_second():
    """Sleep for one tenth of a second."""
    time.sleep(.1)


@app.task()
def one_tenth_second_with_arg(data):
    """Sleep for one tenth of a second."""
    time.sleep(.1)


@app.task(queue="tasks")
def zero_priority():
    """Zero priority."""


@app.task(queue="tasks:9")
def one_priority():
    """One priority."""
