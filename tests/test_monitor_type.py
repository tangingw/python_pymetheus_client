from monitor.monitor_service import MonitorHTTP
from monitor.monitor_sys import MonitorDisk, MonitorCPU
from monitor_type import get_monitor_type


def test_get_monitor_type():

    assert get_monitor_type(MonitorDisk()) == "harddisk"
    assert get_monitor_type(MonitorCPU()) == "cpu"
    assert get_monitor_type(MonitorHTTP("http://127.0.0.1/")) == "http"
