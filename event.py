from datetime import datetime
from os import stat
from monitor_type import get_monitor_type


class MonitorEvent:

    @staticmethod
    def generate_event(
        event_type, monitor_object, device_status, event_value, 
        event_message=None, event_status=None
    ):

        return {
            "event_type": event_type, #Can be http response time
            "event_value": event_value, #single-value event
            "event_message": event_message, #can be a log message
            "monitor_type": get_monitor_type(monitor_object), #To which this service go e.g. service
            "monitor_type_id": device_status[get_monitor_type(monitor_object)], #service id
            "created_at": datetime.utcnow().isoformat()
        }