import os
import json
import pytest
from configuration import PyMetheusConfig


@pytest.fixture
def load_config_module():

    test_str = {
        "url": "http://127.0.0.1:8080"
    }

    pymetheus_config = PyMetheusConfig()
    pymetheus_config.write_config(test_str)

    return test_str, pymetheus_config


def test_pymetheus_config_read(load_config_module):
    
    module_config = load_config_module
    config_data = json.loads(module_config[1].load_config())

    assert config_data["status_code"] == 200
    assert config_data["status_msg"] == "config loaded successfully."

    assert module_config[0]["url"] == config_data["config"]["url"]


def test_config_file_in_folder():

    default_path = "config/config.json"
    assert os.path.exists(default_path)