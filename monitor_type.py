from monitor.monitor_sys import MonitorCPU


class MonitorType:

    monitor_type_db = {
        "MonitorCPU": "device",
        "MonitorMemory": "device",
        "MonitorDisk": "harddisk",
        "MonitorHTTP": "service",
        "MonitorDBMS": "service",
        "MonitorPort": "port",
        "MonitorPlatform": "device",
        "MonitorNetwork": "network",
        "MonitorService": "service"
    } 

    def get_monitor_type(self, monitoring_object):

        return self.monitor_type_db[
            monitoring_object.get_class_name()
        ]

    def add_monitor_type(self, monitoring_object_dict):

        self.monitor_type_db.update(
            monitoring_object_dict
        )