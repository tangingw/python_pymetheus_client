from monitor.monitor_sys import MonitorCPU


def get_monitor_type(monitoring_object):

    return {
        "MonitorCPU": "cpu",
        "MonitorMemory": "memory",
        "MonitorDisk": "harddisk",
        "MonitorHTTP": "http",
        "MonitorDBMS": "db",
        "MonitorPort": "port",
        "MonitorNetwork": "network"
    }[type(monitoring_object).__name__]
