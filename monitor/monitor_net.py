import os
import psutil
import platform
from datetime import datetime
from socket import AF_INET, AF_INET6, SOCK_DGRAM, SOCK_STREAM


class MonitorNetwork:

    def __init__(self):

        self.net_connections = psutil.net_connections()
        self.network_interface_info = psutil.net_if_addrs()

    def get_network_interface(self):

        ip_layer_dict = {
            AF_INET: "ipv4",
            AF_INET6: "ipv6"
        }

        network_interface_dict = {
            interface_name: [
                {
                    "ip_type": ip_layer_dict[intf.family] if intf.family in ip_layer_dict.keys() else "mac-address",
                    "mac_address": intf.address if intf.family not in ip_layer_dict.keys() else None,
                    "ip_address": intf.address.split("%")[0] if intf.family in ip_layer_dict.keys() else None,
                    "netmask": intf.netmask, "broadcast": intf.broadcast
                } for intf in interfaces
            ] for interface_name, interfaces in self.network_interface_info.items()
        }
        
        return network_interface_dict


    def get_connection_process(self):

        protocol_dict = {
            (AF_INET, SOCK_DGRAM): "udp",
            (AF_INET6, SOCK_DGRAM): "udp6",
            (AF_INET6, SOCK_STREAM): "tcp6",
            (AF_INET, SOCK_STREAM): "tcp"
        }

        connection_process = []
        current_process = {
            process.pid: process for process in psutil.process_iter(['pid', 'name', 'username'])
        }

        for p in self.net_connections:

            network_connection_dict = {
                "protocol": protocol_dict[(p.family, p.type)],
                "local_address": f"{p.laddr.ip}:{p.laddr.port}",
                "remote_address": f"{p.raddr.ip}:{p.raddr.port}" if p.raddr else "-"
            }
            if ((platform.system() == "Linux" and os.geteuid() == 0) or platform.system() == "Windows"):

                if p.pid in current_process.keys():

                    network_connection_dict.update(
                        {
                            "process_name": current_process[p.pid].info["name"],
                            "status": current_process[p.pid].status(),
                            "started_at": datetime.fromtimestamp(
                                current_process[p.pid].create_time()
                            ).isoformat(),
                        }
                    )

            connection_process.append(network_connection_dict)
        
        return connection_process

    def get_all_info(self):

        return {
            "network_interfaces": self.get_network_interface(),
            "network_netstats": self.get_connection_process(),
            "network_io": self.get_net_io_counters()
        }

    def get_ping(self, target_ip=None):

        if not target_ip:

            target_ip = "8.8.8.8"

        if platform.system() == "Windows":
            ping_result = os.system(f"ping -n 3 {target_ip}")

        else:
            ping_result = os.system(f"ping -c 3 {target_ip}")
        

        if ping_result > 0:

            return {
                "status": 500,
                "message": "ping failed"
            }
        
        return {
            "status": 200,
            "message": "ping_success"
        }
    
    def get_net_io_counters(self):

        io_counters = psutil.net_io_counters(pernic=True)
        
        return {
            interface: {
                "bytes_sent": interface_io.bytes_sent,
                "bytes_recv": interface_io.bytes_recv,
                "packets_sent": interface_io.packets_sent,
                "packers_recv": interface_io.packets_recv,
                "errin": interface_io.errin,
                "errout": interface_io.errout,
                "dropin": interface_io.dropin,
                "dropout": interface_io.dropout
            }
            for interface, interface_io in io_counters.items()
        }
    
    def get_class_name(self):

        if self.__class__.__base__.__name__ == "object":

            return self.__class__.__name__
        
        return self.__class__.__base__.__name__
