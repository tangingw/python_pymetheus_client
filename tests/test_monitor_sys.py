import pytest
import platform
from monitor.monitor_sys import MonitorCPU
from monitor.monitor_sys import MonitorMemory
from monitor.monitor_sys import MonitorDisk


@pytest.fixture
def get_cpu():

    return MonitorCPU()


@pytest.fixture
def get_memory():

    return MonitorMemory()

@pytest.fixture
def get_storage():

    return MonitorDisk()


def test_get_cpu_data(get_cpu):

    assert isinstance(get_cpu.get_cpu_data(), dict)
    assert "cpu_percent_overall" in get_cpu.get_cpu_data().keys()
    assert "cpu_percent_per_cpu" in get_cpu.get_cpu_data().keys()


def test_get_cpu_percent(get_cpu):

    assert isinstance(get_cpu.get_cpu_percent(), float)


def test_get_memory(get_memory):

    assert isinstance(get_memory.get_memory_data(), dict)
    assert len(
        set(
            get_memory.get_memory_data().keys()
        ).intersection(
            ["total", "available", "usage_percent", "used"]
        )
    ) == 4


def test_get_all_partition(get_storage):

    assert isinstance(get_storage.get_all_partition(), list)

    assert len(
        set(
            get_storage.get_all_partition()[0].keys()
        ).intersection(
            [
                "device", "mount_point", "fstype", "opts"
            ]
        )
    )


def test_get_disk_usage(get_storage):

    mount_point = "/tmp"

    if platform.system() == "Windows":

        mount_point = "C:\\"

    assert isinstance(get_storage.get_disk_usage(mount_point), dict)
    assert len(
        set(
            get_storage.get_disk_usage(mount_point).keys()
        ).intersection(
            set(
                ["path", "total", "used", "free", "used_percentage"]
            )
        )
    )

def test_get_disks_all_data(get_storage):

    assert isinstance(get_storage.get_disk_all_data(), dict)
