from restaurants.serializers import RestaurantSerializer


def test_serializer(db):
    valid_data = {
        'name': 'test',
        'address': 'test',
        'phone': '000-000-00-00',
        'email': 'email@gmail.com'
    }
    serializer = RestaurantSerializer(data=valid_data)
    result = serializer.is_valid()
    assert result is True

    invalid_data = {
        'name': 'test',
        'address': 'test',
        'phone': '000-000-00-00',
        'email': 'email'
    }
    serializer = RestaurantSerializer(data=invalid_data)
    result = serializer.is_valid()
    assert result is False
