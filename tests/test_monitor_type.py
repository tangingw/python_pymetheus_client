from monitor.monitor_service import MonitorHTTP
from monitor.monitor_sys import MonitorDisk, MonitorCPU
from monitor_type import MonitorType


def test_get_monitor_type(): #need to rewrite again

    monitor_type = MonitorType()
    assert monitor_type.get_monitor_type(MonitorDisk()) == "harddisk"
    assert monitor_type.get_monitor_type(MonitorCPU()) == "device"
    assert monitor_type.get_monitor_type(MonitorHTTP("http://127.0.0.1/")) == "service"
