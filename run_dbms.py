import time
from monitor.monitor_sys import MonitorMemory
from monitor.monitor_service import MonitorDBMS
from event import MonitorEvent


class MonitorMyDBMS:

    def __init__(self):
        self.monitor_dbms = MonitorDBMS('5432', service_name="PostgreSQL DB")
        self.monitor_dbms.connect_db(
            {
                "server": "192.168.0.179",
                "database": "postgres",
                "user": "postgres",
                "password": "tallgeese3"
            }
        )
        self.monitor_event = MonitorEvent()
        self.monitor_memory = MonitorMemory()

    def get_memory_info(self, queue, wait_time):

        while queue.empty():

            self.monitor_event.post_event(
                "memory", self.monitor_memory,
                self.monitor_memory.get_memory_data()["host_name"],
                event_value=self.monitor_memory.get_memory_data()["usage_percent"]
            )
        
            time.sleep(wait_time)


    def get_postgre_status(self, queue, wait_time):

        while queue.empty():
            
            dbms_return_status = self.monitor_dbms.get_status()
        
            self.monitor_event.post_event(
                "postgresql status", self.monitor_dbms,
                self.monitor_dbms.get_service_metadata()["service_name"], 
                event_status=dbms_return_status["status_code"],
                event_message=dbms_return_status["status_msg"],
                event_value=dbms_return_status["status_value"]
            )

            time.sleep(wait_time)


    def get_postgre_connection(self, queue, wait_time):

        while queue.empty():

            dbms_return_connection = self.monitor_dbms.get_connection_count()

            self.monitor_event.post_event(
                "postgresql connection count", self.monitor_dbms,
                self.monitor_dbms.get_service_metadata()["service_name"], 
                event_status=dbms_return_connection["status_code"],
                event_message=dbms_return_connection["status_msg"],
                event_value=dbms_return_connection["status_value"]
            )

            time.sleep(wait_time)
