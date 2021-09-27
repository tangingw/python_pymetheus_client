from datetime import datetime
from monitor_type import MonitorType
from client import PyMetheusDeviceClient

class MonitorEvent:
    
    def __init__(self):

        self.client = PyMetheusDeviceClient()
        self.client.select_endpoint("/collect")

    def generate_event(
        self, event_type, 
        monitor_object, monitor_type_name, event_value=None, 
        event_message=None, event_status=None
    ):

        """
        monitor_type_name
        
        can borrow from register_device
        for monitor_type_name reference,
        "MonitorCPU": "device hostname, host_name",
        "MonitorMemory": "device hostname, host_name",
        "MonitorDisk": "hdd name, name e.g. C:\\ for windows /dev/sda1 for mount point",
        "MonitorHTTP": "service name, service_name",
        "MonitorDBMS": "service name, service_name",
        "MonitorPort": "port num, port",
        "MonitorPlatform": "device hostname, host_name",
        "MonitorNetwork": "ip address, ip_address",
        "MonitorService": "service name, service_name"
        """
        return {
            "event_type": event_type, #Can be http response time
            "event_value": event_value, #single-value event
            "event_message": event_message, #can be a log message
            "event_status": event_status,
            "monitor_type": MonitorType().get_monitor_type(monitor_object), #To which this service go e.g. service
            "monitor_type_name": monitor_type_name, #Name of monitor object that you are monitoring
            "created_at": datetime.utcnow().isoformat()
        }
    
    def post_event(
        self, event_type, 
        monitor_object, monitor_type_name, event_value=None, 
        event_message=None, event_status=None
    ):

        my_event = self.generate_event(
            event_type, 
            monitor_object, monitor_type_name, event_value=event_value, 
            event_message=event_message, event_status=event_status
        )

        self.client.post_data(my_event)


