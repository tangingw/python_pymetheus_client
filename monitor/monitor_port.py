import socket
from utils import return_status


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

    def get_status(self):

        socket_proto_type = socket.SOCK_STREAM
        
        if self.service_proto in ["udp", "udp6"]:

            socket_proto_type = socket.SOCK_DGRAM

        socket.setdefaulttimeout(1)
        sock_connection = socket.socket(socket.AF_INET, socket_proto_type)

        try:
            sock_connection.connect((self.ip_address, int(self.service_port)))

        except (ConnectionRefusedError, TimeoutError, OSError) as error_msg:

            return return_status(500, error_msg)

        else:
            return return_status(200, "success")

        