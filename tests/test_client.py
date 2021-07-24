import pytest
from client import PyMetheusDevice
from tests.mock_server import start_mock_server


@pytest.fixture
def load_device_client():
    start_mock_server()
    return PyMetheusDevice()


def test_load_config(load_device_client):

    assert isinstance(load_device_client.config, dict)


def test_client_get(load_device_client):

    response_data = load_device_client.get_data()
    assert response_data["status_code"] == 200
    assert response_data["response_msg"]["message"] == "this is from a mock server"


def test_client_post(load_device_client):

    test_data = {"message": "HI"}
    response_data = load_device_client.post_data(test_data)
    assert response_data["status_code"] == 200
    assert response_data["response_msg"]["message"] == "OK"
