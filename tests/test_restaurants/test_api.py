def test_api(db, client):
    r = client.get('/restaurants/')
    assert r.status_code == 200

    r = client.post('/restaurants/', data={
        'name': 'test',
        'address': 'test address',
        'phone': '000-000-00-00',
        'email': 'test@gmail.com'
    })

    assert r.status_code == 401
