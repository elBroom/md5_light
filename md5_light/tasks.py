from sqlalchemy.sql import func

from md5_light import app, celery, db
from md5_light.models import Task, StatusType
from md5_light.utils import (
    DownloadFileException, 
    calculate_hash_by_file, 
    dowanload_file, 
    remove_file, 
    send_email
)


@celery.task
def calculate_hash_by_url_task(task_uuid):
    task = Task.query.filter_by(id=task_uuid).first()
    if not task:
        return

    task.status = StatusType.RUNNING
    task.started_at = func.now()
    db.session.commit()

    try:
        task.md5 = get_hash(task.url)
    except Exception:
        task.status = StatusType.FAIL
    else:
        task.status = StatusType.DONE
    task.finished_at = func.now()
    db.session.commit()

    if app.config['EMAIL_ENABLED'] and task.email:
        text = (
            'A file with URL ({}) has hash: {}.'.format(task.url, task.md5)
            if task.status == StatusType.DONE
            else  'A file with URL ({}) is not loaded.'.format(task.url)
        )
        send_email(
            host=app.config['EMAIL_HOST'],
            subject='Task is done',
            to_addr=task.email,
            from_addr=app.config['EMAIL_FROM_ADDR'],
            body_text=text,
        )

def get_hash(url):
    path = dowanload_file(url)
    md5 = calculate_hash_by_file(path)
    remove_file(path)
    return md5
