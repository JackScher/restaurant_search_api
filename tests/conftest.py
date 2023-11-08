import pytest


@pytest.fixture
def get_token(db, client) -> str:
    client.post('/employees/', data={
        'username': 'testadmin',
        'password': 'testadmin',
        'is_admin': True
    })

    r = client.post('/api/token/', data={
        'username': 'testadmin',
        'password': 'testadmin'
    })

    return r.data['access']
