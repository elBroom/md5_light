def test_create_task(test_client, init_database, mocker):
    mocker.patch('md5_checker.tasks.calculate_hash_by_url_task')
    mocker.patch('md5_checker.schema.get_task_id', lambda: 'uuid_test')

    response = test_client.post(
        '/submit',
        data={'email': 'user@example.com', 'url': 'http://site.com/file.txt'},
    )

    assert response.status_code == 200
    assert response.data == b'{"id":"uuid_test"}\n'


def test_get_task(test_client, init_database):
    response = test_client.get('/check/1234')
    assert response.status_code == 200
