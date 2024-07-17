import time

import pytest

from celery_test.tasks.timed_tasks import one_tenth_second, one_tenth_second_with_arg


@pytest.mark.repeat(5)
def test_schedule_1000_tasks():
    start_time = time.time()
    for _ in range(1000):
        one_tenth_second.delay()
    duration = time.time() - start_time
    print(f"Duration: {duration:.3f}")


@pytest.mark.repeat(5)
def test_schedule_1000_tasks_many_data():
    much_data = {i: i**2 for i in range(500)}
    
    start_time = time.time()
    for _ in range(1000):
        one_tenth_second_with_arg.delay(data=much_data)
    duration = time.time() - start_time
    print(f"Duration: {duration:.3f}")