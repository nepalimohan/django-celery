from celery import shared_task

@shared_task #@app.task will also work but you will have to import it
def task1():
    return "task 1"


@shared_task #@app.task will also work but you will have to import it
def task2():
    return "task 2 "