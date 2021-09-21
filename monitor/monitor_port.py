import socket


class MonitorPort:

    def __init__(self, port, port_description):

        self.port = port
        self.port_description = port_description
    
    def get_port_data(self):

        return {
            "port": self.port,
            "port_desc": self.port_description
        }
    
    def get_port_status(self, ip_address, port):

        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_status = my_socket.connect_ex((ip_address, port))

        return port_status

        