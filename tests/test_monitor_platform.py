import pytest
from monitor.monitor_platform import MonitorPlatform


@pytest.fixture
def create_platform():

    return MonitorPlatform().get_platform_info()


def test_platform(create_platform):

    assert len(
        set(
            create_platform.keys()
        ).intersection(set(
            [
                "system", "machine_name", "release", "version", 
                "architecture", "processor_type", "python_version"
            ]
        ) 
    )) == 7

    if create_platform["system"] == "Windows":

        assert "windows_version" in create_platform.keys()
    
    if create_platform["system"] == "Darwin":

        assert "mac_version" in create_platform.keys()