from dishes.serializers import DishSerializer


def test_serializer(db):
    valid_data = {
        'name': 'test dish'
    }
    serializer = DishSerializer(data=valid_data)
    result = serializer.is_valid()
    assert result is True

    invalid_data = {
        'name': True
    }
    serializer = DishSerializer(data=invalid_data)
    result = serializer.is_valid()
    assert result is False
