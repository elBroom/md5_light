import pytest
from md5_checker import api, db

from md5_checker.models import Task


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

    db.session.add(Task(id='1234', url='http://site.com/file.txt'))
    db.session.commit()

    yield db

    db.drop_all()
