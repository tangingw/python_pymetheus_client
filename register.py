from datetime import datetime
from monitor.monitor_platform import MonitorPlatform
from monitor.monitor_sys import MonitorMemory
from monitor.monitor_sys import MonitorDisk


class RegisterDeviceHandler:

    def __init__(self):
        self._device_info = MonitorPlatform().get_platform_info()
        self._device_memory = MonitorMemory().get_memory_data()

    def register(self):

        return {
            "host_name": self._device_info["machine_name"],
            "cpu": self._device_info["architecture"],
            "os_install": self._device_info["system"],
            "memory": self._device_memory["total"],
            "harddisc_size": None,
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }

    def verify_id(self):

        return {
            "host_name": self._device_info["machine_name"]
        }
        #if device is stored on database, it should show an id
        #if no id, then register the device
