import time
from monitor.monitor_sys import MonitorMemory
from monitor.monitor_service import MonitorDBMS
from event import MonitorEvent
from utils import add_function_daemon


monitor_dbms = MonitorDBMS('5432', service_name="PostgreSQL DB")
monitor_dbms.connect_db(
    {
        "server": "192.168.0.179",
        "database": "postgres",
        "user": "postgres",
        "password": "tallgeese3"
    }
)


def get_memory_info(queue, wait_time):

    monitor_event = MonitorEvent()
    monitor_memory = MonitorMemory()

    while True:

        if not queue.empty():

            break

        print(
            monitor_event.generate_event(
                "memory", monitor_memory,
                monitor_memory.get_memory_data()["host_name"],
                event_status=monitor_memory.get_memory_data()["usage_percent"]
            )
        )

        time.sleep(wait_time)


def get_postgre_status(queue, wait_time):

    monitor_event = MonitorEvent()

    while True:

        if not queue.empty():

            break
        
        dbms_return_status = monitor_dbms.get_status()
    
        monitor_event.post_event(
            "postgresql status", monitor_dbms,
            monitor_dbms.get_service_metadata()["service_name"], 
            event_status=dbms_return_status["status_code"],
            event_message=dbms_return_status["status_msg"],
            event_value=dbms_return_status["status_value"]
        )

        time.sleep(wait_time)


def get_postgre_connection(queue, wait_time):

    monitor_event = MonitorEvent()

    while True:

        if not queue.empty():

            break

        dbms_return_connection = monitor_dbms.get_connection_count()

        monitor_event.post_event(
            "postgresql connection count", monitor_dbms,
            monitor_dbms.get_service_metadata()["service_name"], 
            event_status=dbms_return_connection["status_code"],
            event_message=dbms_return_connection["status_msg"],
            event_value=dbms_return_connection["status_value"]
        )

        time.sleep(wait_time)


if __name__ == "__main__":

    add_function_daemon(
        [
            (get_postgre_connection, 1), 
            (get_postgre_status, 5),
            (get_memory_info, 5)
        ]
    )