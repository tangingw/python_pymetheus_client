from monitor.monitor_sys import MonitorCPU


def get_monitor_type(monitoring_object):

    return {
        "MonitorCPU": "device",
        "MonitorMemory": "device",
        "MonitorDisk": "device",
        "MonitorHTTP": "service",
        "MonitorDBMS": "service",
        "MonitorPort": "port",
        "MonitorNetwork": "network",
        "MonitorService": "service"
    }[monitoring_object.get_class_name()]
