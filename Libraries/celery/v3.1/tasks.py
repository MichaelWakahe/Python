from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='amqp://user1:password1@localhost:5672/vhost1')

@app.task
def add(x, y):
    return x + y