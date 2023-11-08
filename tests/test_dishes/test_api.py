def test_api(db, client):
    r = client.get('/dishes/')
    assert r.status_code == 200

    r = client.post('/restaurants/', data={
        'name': 'test dish',
    })

    assert r.status_code == 401
