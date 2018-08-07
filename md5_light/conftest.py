import pytest

from md5_light import api, db
from md5_light.models import StatusType, Task


@pytest.fixture(scope='module')
def test_client():
    app = api.app
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI_TEST']
    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    db.create_all()

    db.session.add(Task(id='test_calculate_hash_by_url_task_done', url='http://site.com/file.txt'))
    db.session.add(Task(id='test_calculate_hash_by_url_task_fail', url='http://site.com/file.txt'))
    db.session.add(Task(id='created123', url='http://site.com/file.txt', status=StatusType.CREATED))
    db.session.add(Task(id='running123', url='http://site.com/file.txt', status=StatusType.RUNNING))
    db.session.add(Task(id='fail123', url='http://site.com/file.txt', status=StatusType.FAIL))
    db.session.add(Task(id='done123', url='http://site.com/file.txt', status=StatusType.DONE, md5='hash'))
    db.session.commit()

    yield db

    db.drop_all()
