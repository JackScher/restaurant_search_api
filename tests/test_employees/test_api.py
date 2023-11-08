from employees.models import Employee


def test_employee_api(db, client):
    r = client.get('/employees/')
    assert r.status_code == 200

    employees = Employee.objects.all()
    assert len(employees) == 0

    r = client.post('/employees/', data={
        'username': 'test',
        'password': 'test'
    })
    assert r.status_code == 201
    e = Employee.objects.get(username='test')
    assert e.id == 1
    assert e.username == 'test'
    assert e.password != 'test'
