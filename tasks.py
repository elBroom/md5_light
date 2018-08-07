import hashlib
import time

from sqlalchemy.sql import func

from md5_checker import celery, db
from md5_checker.models import Task, StatusType


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
    except Exception as e:
        task.status = StatusType.FAIL
    else:
        task.status = StatusType.DONE
    task.finished_at = func.now()
    db.session.commit()


def get_hash(url):
    time.sleep(60)
    return hashlib.md5(url.encode('utf-8')).hexdigest()
