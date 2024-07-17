from celery_test.tasks.timed_tasks import one_priority, zero_priority


def test_priority():
    for _ in range(500):
        one_priority.delay()
    
    for _ in range(500):
        zero_priority.delay()


def test_priority_reversed():
    for _ in range(500):
        zero_priority.delay()
    
    for _ in range(500):
        one_priority.delay()
