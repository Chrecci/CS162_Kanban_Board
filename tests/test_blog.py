import pytest
from KanbanFlask.db import get_db


def test_index(client, auth):
    response = client.get('/')
    assert b'create' not in response.data
    assert b'update' not in response.data
    assert b"Log In" in response.data
    assert b"Register" in response.data

    # After a user logs in, they should be able to create, but no update option yet on index page
    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'Chrecci & Co. Kanban Board' in response.data
    assert b'create' in response.data
    assert b'update' not in response.data
    assert b'view_post' not in response.data

@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/delete',
))

def test_login_required(client, path):
    response = client.post(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'


def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403
    # current user doesn't see edit link
    assert b'href="/1/update"' not in client.get('/').data


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/delete',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404

def test_create_then_update(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'task_status': 'DONE', 'assignee': 'test', 'body': 'body'})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2
    
    assert client.get('/2/update').status_code == 200
    client.post('/2/update', data={'title': 'updated', 'task_status': 'DONE', 'assignee': 'test', 'body': 'body'})

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 2').fetchone()
        assert post['title'] == 'updated'

@pytest.mark.parametrize('path', (
    '/create',
    '/2/update',
))
def test_create_update_validate(client, auth, path, app):
    auth.login()
    #response = client.post(path, data={'title': '', 'task_status': 'DONE', 'assignee': 'test', 'body': 'body'})
    #assert b'Title is required.' in response.data

    client.post('/create', data={'title': '2nd post', 'task_status': 'DONE', 'assignee': 'test', 'body': 'body'})
    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 2').fetchone()
        assert post['title'] == '2nd post'
    response = client.post(path, data={'title': '', 'task_status': 'DONE', 'assignee': 'test', 'body': 'body'})
    assert b'Title is required.' in response.data

def test_delete(client, auth, app):
    auth.login()
    client.post('/create', data={'title': '2nd post', 'task_status': 'DONE', 'assignee': 'test', 'body': 'body'})
    response = client.post('/2/delete')

    #after deletion, should redirect to main board. Also no more post in database
    assert response.headers['Location'] == 'http://localhost/board/main_board'
    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 2').fetchone()
        assert post is None

def test_view_post(client, auth, app):

    #if user not logged in, should be redirected to login page when trying to view post
    response = client.get('2/view_post') 
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/auth/login'

    #if logged in succesfully, show post
    auth.login()
    client.post('/create', data={'title': '2nd post', 'task_status': 'DONE', 'assignee': 'test', 'body': 'body'})
    response = client.get('2/view_post')
    assert response.status_code == 200
    assert b'Task Status' in response.data
