"""
Ensure you have RabbitMQ running locally.

To start the worker, from within the top level project folder named 'celery', run:
    celery -A v4_4_7.tasks worker --loglevel=info

From a Python console which has the 'celery' folder as the PYTHONPATH:
    >>> from v4_4_7.tasks import add
    >>> add.delay(4, 4)
"""
from celery import Celery


# app = Celery('tasks', broker='amqp://guest@localhost//')  # No results backend

"""Note that the 'redis' Python library is required if specifying a Redis results backend. """
app = Celery('tasks', backend='redis://localhost', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
