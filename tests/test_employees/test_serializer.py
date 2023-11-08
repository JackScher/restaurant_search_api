from employees.serializers import EmployeeSerializer


def test_serializer(db):
    valid_data = {
        'username': 'test',
        'email': 'email@gmail.com',
        'password': 'test'
    }
    serializer = EmployeeSerializer(data=valid_data)
    result = serializer.is_valid()
    assert result is True

    invalid_data = {
        'username': 'test',
        'email': 'email',
        'password': 'test'
    }
    serializer = EmployeeSerializer(data=invalid_data)
    result = serializer.is_valid()
    assert result is False
