from datetime import datetime
from os import stat
from monitor_type import get_monitor_type


class MonitorEvent:

    @staticmethod
    def generate_event(monitor_object, event_value, event_message=None):

        return {
            "monitor_type": get_monitor_type(monitor_object),
            "event_value": event_value,
            "event_message": event_message,
            "created_at": datetime.utcnow().isoformat()
        }