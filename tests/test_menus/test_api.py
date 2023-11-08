def test_api(db, client):
    r = client.get('/menus/')
    assert r.status_code == 200

    r = client.post('/restaurants/', data={
        'price': 100,
        'restaurant': 1,
    })

    assert r.status_code == 401
