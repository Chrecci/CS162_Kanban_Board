import pytest
from KanbanFlask.db import get_db
from collections import Counter

def test_main_board(client, auth):
    response = client.get('/board/main_board')
    assert b'Please sign in' in response.data
    assert b'create' not in response.data
    assert b"Log In" in response.data
    assert b"Register" in response.data

    #if user is not loggged in, there should be no board displyed, so no columns
    assert b'column' not in response.data

    auth.login()
    response = client.get('/board/main_board')
    assert b'create' in response.data
    assert b'column' in response.data

    #make sure that each column exists after user logs in
    statuses = ["Blocked", "To Define", "TODO", "In Progress", "QA Review", "PO Review", "Done!"]
    for i in statuses:
        assert bytes(i, encoding='utf8') in response.data

def test_user_board(client, auth):

    #user should not be able to acces user_board unless signed in. Should redirect to login page
    response = client.get('/board/user_board')
    assert response.headers['Location'] == 'http://localhost/auth/login'
    assert b'create' not in response.data

    #if user is not loggged in, there should be no board displyed, so no columns
    assert b'column' not in response.data

    auth.login()
    response = client.get('/board/user_board')
    assert b'create' in response.data
    assert b'column' in response.data

    #make sure that each column exists after user logs in
    statuses = ["Your Tickets", "You Assigned"]
    for i in statuses:
        assert bytes(i, encoding='utf8') in response.data
