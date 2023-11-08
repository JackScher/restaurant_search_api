def test_api(db, client):
    r = client.get('/votes/')
    assert r.status_code == 200

    r = client.post('/restaurants/', data={
        'employee': 1,
        'menu': 1,
    })

    assert r.status_code == 401
