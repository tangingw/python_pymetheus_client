from monitor.monitor_sys import MonitorCPU
from monitor.monitor_sys import MonitorMemory
from monitor.monitor_platform import MonitorPlatform
from event import MonitorEvent


def test_cpu_event():

    my_cpu = MonitorCPU()
    event_object = MonitorEvent().generate_event(
        "cpu", my_cpu, 
        MonitorPlatform().get_platform_info()["machine_name"],
        event_value=my_cpu.get_cpu_percent()
    )

    assert isinstance(event_object, dict)
    assert "event_value"in event_object.keys()
    assert isinstance(event_object["event_value"], float)


def test_memory_event(): #Need to rewrite the tests

    my_memory = MonitorMemory()
    event_object = MonitorEvent().generate_event(
        "memory", my_memory,
        MonitorPlatform().get_platform_info()["machine_name"], 
        event_value=my_memory.get_memory_data()["usage_percent"]
    )

    assert isinstance(event_object, dict)
    assert "event_value"in event_object.keys()
    assert isinstance(event_object["event_value"], float)