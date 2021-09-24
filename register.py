import hashlib
import json
from datetime import datetime
from monitor.monitor_platform import MonitorPlatform
from monitor.monitor_sys import MonitorMemory
from monitor.monitor_sys import MonitorDisk
from monitor.monitor_net import MonitorNetwork
from monitor.monitor_port import MonitorPort
from monitor.monitor_service import MonitorDBMS
from configuration import PyMetheusConfig
from client import PyMetheusDeviceClient


class RegisterDeviceHandler:

    def __init__(self):
        self._device_info = MonitorPlatform().get_platform_info()
        self._device_memory = MonitorMemory().get_memory_data()
        self._device_hdd = MonitorDisk().get_disk_metadata()
        self._device_network = MonitorNetwork().get_network_interface()
        self.client = PyMetheusDeviceClient()

        self._device_default_meta = {
            "host_name": self._device_info["machine_name"],
            "cpu": self._device_info["architecture"],
            "os_install": self._device_info["system"],
            "memory": self._device_memory["total"],
            "harddisc": self._device_hdd,
            "network": self._device_network,
            "ports": [],
            "services": []
        }

    def add_service(self, service_list):
        """[
                MonitorDBMS(
                    5432, service_desc="PostgreSQL"
                ).get_service_metadata()
            ],
        """
        self._device_default_meta["services"] = service_list

    def add_port(self, port_list):
        """
        [
            MonitorDBMS(
                5432, service_desc="PostgreSQL"
            ).get_service_metadata()
        ]
        """
        self._device_default_meta["ports"] = port_list    

    def get_device_metadata(self):

        return self._device_default_meta

    def get_device_id(self):
        """
        if device is stored on database, it should show an id
        if no id, then register the device

        question: what if the device has a new interface/service/port?
        answer: check device property sha256 hash. if different then we post
        """
        return {
            "host_name": self._device_info["machine_name"]
        }
    
    def delete_device(self):
        """
        For further development
        """
        pass
        
    def generate_sha256_hash(self):

        return hashlib.sha256(
            json.dumps(
                self.get_device_metadata()
            ).encode("utf-8")
        ).hexdigest()

    def register(self):

        self.client.select_endpoint("/register")

        if not self.compare_hash():
            self.client.post_data(
                data=self.get_device_metadata()
            )

        register_hash = self.generate_sha256_hash()
        self.client.write_config(
            {
                "url": self.client.main_url,
                "register_hash": register_hash
            }
        )
    
    def compare_hash(self):

        new_hash = self.generate_sha256_hash()
        current_hash = self.client.get_config()["config"].get("register_hash")

        if current_hash:

            return new_hash == current_hash

        return False