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


@app.task()
def one_second():
    """Sleep for one second."""
    time.sleep(1)