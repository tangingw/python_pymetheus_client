from register import RegisterDeviceHandler
from monitor.monitor_service import MonitorDBMS
from monitor.monitor_port import MonitorPort
from run_dbms import MonitorMyDBMS
from utils import add_function_daemon


register_device = RegisterDeviceHandler()
device_id = register_device.get_device_id()

register_device.add_service(
    [
        MonitorDBMS(
            5432, service_desc="PostgreSQL on RPI 3B", service_name="Raspi3 PostgreSQL DB"
        ).get_service_metadata()
    ]
)

register_device.add_port(
    [
        MonitorPort(
            "192.168.200.188", 5432, "PostgreSQL DB"
        ).get_port_data()
    ]
)


register_device.register()

my_monitoring = MonitorMyDBMS()
add_function_daemon(
    [
        (my_monitoring.get_postgre_connection, 60), 
        (my_monitoring.get_postgre_status, 60),
        (my_monitoring.get_memory_info, 60)
    ]
)
