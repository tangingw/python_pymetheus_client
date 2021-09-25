import hashlib
import json
import os
from monitor.monitor_platform import MonitorPlatform
from monitor.monitor_sys import MonitorMemory
from monitor.monitor_sys import MonitorDisk
from monitor.monitor_net import MonitorNetwork
from monitor.monitor_port import MonitorPort
from monitor.monitor_service import MonitorDBMS
from configuration import PyMetheusConfig
from client import PyMetheusDeviceClient


class RegisterDeviceHandler:

    def __init__(self, register_config=None):

        if register_config:
            self.register_config = register_config

        else:
            self.register_config = "config/register.json"

        self.client = PyMetheusDeviceClient()    
        self.load_register()

    def generate_device_meta(self):

        device_info = MonitorPlatform().get_platform_data()
        device_memory = MonitorMemory().get_memory_data()
        device_hdd = MonitorDisk().get_disk_metadata()
        device_network = MonitorNetwork().get_network_interface()

        self._device_default_meta = {
            "host_name": device_info["machine_name"],
            "cpu": device_info["architecture"],
            "os_install": device_info["system"],
            "memory": device_memory["total"],
            "harddisc": device_hdd,
            "network": device_network,
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
        for service_item in service_list:

            if not (service_item in self._device_default_meta["services"]):
                self._device_default_meta["services"].append(service_item)

    def add_port(self, port_list):
        """
        [
            MonitorDBMS(
                5432, service_desc="PostgreSQL"
            ).get_service_metadata()
        ]
        """
        for port_item in port_list:

            if not (port_item in self._device_default_meta["ports"]):
                self._device_default_meta["ports"].append(port_item)    

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
            "register_hash": self.client.get_config()["config"].get("register_hash")
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

        if not self.compare_hash():
            self.client.select_endpoint("/register")

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

            self.save_register()

    def load_register(self):

        device_register_str = None
        if os.path.exists(self.register_config):
            
            self._device_default_meta = {}
            
            with open(self.register_config, "r") as register_json:

                device_register_str = register_json.read()

        if device_register_str:
            self._device_default_meta = json.loads(device_register_str)
        
        else:
            self.generate_device_meta()

    def save_register(self):

        with open(self.register_config, "w", newline="") as register_json:

            register_json.write(
                json.dumps(
                    self.get_device_metadata(),
                    indent=4
                )
            )

    def compare_hash(self):

        new_hash = self.generate_sha256_hash()
        current_hash = self.get_device_id()["register_hash"]

        if current_hash:

            return new_hash == current_hash

        return False