from monitor.monitor_service import MonitorDBMS
from event import MonitorEvent
from utils import add_function_daemon


monitor_dbms = MonitorDBMS('5432', service_name="postgresql db")
monitor_dbms.connect_db(
    {
        "server": "192.168.0.179",
        "database": "postgres",
        "user": "postgres",
        "password": "tallgeese3"
    }
)


def get_postgre_status():
    monitor_event = MonitorEvent()
    dbms_return_status = monitor_dbms.get_status()
    
    monitor_event.post_event(
        MonitorEvent().generate_event(
            "postgresql status", monitor_dbms,
            monitor_dbms.get_service_metadata()["service_name"], 
            event_status=dbms_return_status["status_code"],
            event_message=dbms_return_status["status_msg"],
            event_value=dbms_return_status["status_value"]
        )
    )


def get_postgre_connection():

    monitor_event = MonitorEvent()
    dbms_return_connection = monitor_dbms.get_connection_count()

    monitor_event.post_event(
        MonitorEvent().generate_event(
            "postgresql connection count", monitor_dbms,
            monitor_dbms.get_service_metadata()["service_name"], 
            event_status=dbms_return_connection["status_code"],
            event_message=dbms_return_connection["status_msg"],
            event_value=dbms_return_connection["status_value"]
        )
    )


if __name__ == "__main__":

    add_function_daemon([get_postgre_connection, get_postgre_status])