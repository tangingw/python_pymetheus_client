from datetime import datetime
from monitor.monitor_platform import MonitorPlatform
from monitor.monitor_sys import MonitorMemory
from monitor.monitor_sys import MonitorDisk
from monitor.monitor_net import MonitorNetwork
from monitor.monitor_port import MonitorPort
from monitor.monitor_service import MonitorDBMS


class RegisterDeviceHandler:

    def __init__(self):
        self._device_info = MonitorPlatform().get_platform_info()
        self._device_memory = MonitorMemory().get_memory_data()
        self._device_hdd = MonitorDisk().get_disk_all_data()
        self._device_network = MonitorNetwork().get_network_interface()

        self._device_default_meta = {
            "host_name": self._device_info["machine_name"],
            "cpu": self._device_info["architecture"],
            "os_install": self._device_info["system"],
            "memory": self._device_memory["total"],
            "harddisc": self._device_hdd,
            "network": self._device_network,
            "port": [
                MonitorPort(5432, "PostgreSQL").get_port_data(),
 
            ],
            "service": [
                MonitorDBMS(
                    "", 5432, service_desc="PostgreSQL"
                ).get_service_metadata()
            ],
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }

    def add_service(self, service_dict):

        self._device_default_meta.update(service_dict)
    
    def get_device(self):

        return self._device_default_meta

    def get_device_id(self):

        return {
            "host_name": self._device_info["machine_name"]
        }
        #if device is stored on database, it should show an id
        #if no id, then register the device
