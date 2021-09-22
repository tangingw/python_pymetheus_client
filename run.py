from register import RegisterDeviceHandler
from monitor.monitor_sys import MonitorMemory
from client import PyMetheusDevice
from event import MonitorEvent


register_device = RegisterDeviceHandler()
device_id = register_device.get_device_id()

pymetheus_client = PyMetheusDevice()
pymetheus_client.select_endpoint("/register")

"""
pymetheus_client.select_endpoint(f"/device/{device_id}")
device_status = pymetheus_client.get_data(device_id)

if not device_status:
    print(
        "Device Not Registered"
    )

    pymetheus_client.select_endpoint("/device")
    pymetheus_client.post_data(
        data=register_device.get_device()
    )

else:

    #if monitor type is not in monitor_type table, add into table
    pymetheus_client.select_endpoint("/collect")
    pymetheus_client.post_data(
        data=MonitorEvent.generate_event(
            "Memory", MonitorMemory, 
            device_status, event_value=4
        )
    )

    print("Send Event Data")
"""

#pymetheus_client.select_endpoint("/device")
pymetheus_client.post_data(
    data=register_device.get_device_metadata()
)