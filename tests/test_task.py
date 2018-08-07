from md5_checker.models import StatusType, Task
from md5_checker.tasks import calculate_hash_by_url_task


def test_calculate_hash_by_url_task_done(init_database, mocker):
    mocker.patch('md5_checker.tasks.get_hash', lambda _: 'hash')

    task_uuid = 'test_calculate_hash_by_url_task_done'
    calculate_hash_by_url_task(task_uuid)
    task = Task.query.filter_by(id=task_uuid).first()
    assert task.status == StatusType.DONE


def test_calculate_hash_by_url_task_fail(init_database, mocker):
    mocker.patch('md5_checker.tasks.get_hash', lambda: 1)

    task_uuid = 'test_calculate_hash_by_url_task_fail'
    calculate_hash_by_url_task(task_uuid)
    task = Task.query.filter_by(id=task_uuid).first()
    assert task.status == StatusType.FAIL
