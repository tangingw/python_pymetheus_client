from monitor.monitor_sys import MonitorCPU
from monitor.monitor_sys import MonitorMemory
from event import MonitorEvent


def test_cpu_event():

    my_cpu = MonitorCPU()
    event_object = MonitorEvent.generate_event(
        my_cpu, my_cpu.get_cpu_percent()
    )

    assert isinstance(event_object, dict)
    assert "event_value"in event_object.keys()
    assert isinstance(event_object["event_value"], float)


def test_memory_event():

    my_memory = MonitorMemory()
    event_object = MonitorEvent.generate_event(
        my_memory, my_memory.get_memory_data()["usage_percent"]
    )

    assert isinstance(event_object, dict)
    assert "event_value"in event_object.keys()
    assert isinstance(event_object["event_value"], float)