import time
#from register import RegisterDeviceHandler
from monitor.monitor_sys import MonitorMemory
from monitor.monitor_sys import MonitorCPU
from event import MonitorEvent
#from monitor.monitor_platform import MonitorPlatform
from monitor.monitor_service import MonitorDBMS


"""monitor_dbms = MonitorDBMS("5432", service_desc="PostgreSQL", service_name="PostgreSQL DB")
print(
    monitor_dbms.get_service_metadata()
)

monitor_dbms.connect_db(
    {
        "database": "postgres",
        "user": "postgres",
        "password": "",
        "server": "192.168.0.179"
    }
)
"""


print(
    MonitorCPU().get_cpu_data()
)
monitor_cpu = MonitorCPU()
monitor_event = MonitorEvent()

while True:
        
    print(monitor_cpu.get_cpu_percent())
    monitor_event.post_event(
        "cpu", monitor_cpu,
        monitor_cpu.get_cpu_data()["host_name"],
        event_value=monitor_cpu.get_cpu_percent()
    )

    """dbms_return_status = monitor_dbms.get_status()

    print(
        MonitorEvent.generate_event(
            "postgresql", monitor_dbms,
            monitor_dbms.get_service_metadata()["service_name"], 
            event_status=dbms_return_status["status_code"],
            event_message=dbms_return_status["status_msg"]
        )
    )
    """

    time.sleep(1)