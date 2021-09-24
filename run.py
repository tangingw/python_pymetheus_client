import hashlib
import json
from register import RegisterDeviceHandler
from monitor.monitor_service import MonitorDBMS
from monitor.monitor_port import MonitorPort
from event import MonitorEvent


register_device = RegisterDeviceHandler()
device_id = register_device.get_device_id()

register_device.add_service(
    [
        MonitorDBMS(
            5432, service_desc="PostgreSQL", service_name="PostgreSQL DB"
        ).get_service_metadata()
    ]
)

register_device.add_port(
    [
        MonitorPort(
            "192.168.200.190", 5432, "PostgreSQL DB"
        ).get_port_data()
    ]
)

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

register_device.register()