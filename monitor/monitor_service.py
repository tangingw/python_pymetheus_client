import socket
import requests
import importlib


def return_status(status_code, status_msg):

    return {
        "status_code": status_code,
        "status_msg": status_msg
    }


class MonitorService:

    def __init__(self, service_port, service_proto, service_url=None, service_desc=None):

        self.service_desc = service_desc
        self.service_port = service_port
        self.service_proto = service_proto
        self.service_url = service_url
    
    def get_service_metadata(self):

        return {
            "service_desc": self.service_desc,
            "service_port": self.service_port,
            "service_proto": self.service_proto
        }

    def get_status(self):
        """
        To be overriden by daughter class
        """
        pass

    def get_response_time(self):
        """
        To be overriden by daughter class
        """
        pass

    def get_class_name(self):

        if self.__class__.__base__.__name__ != "object":

            return self.__class__.__name__
        
        return self.__class__.__base__.__name__


class MonitorHTTP(MonitorService):

    def __init__(self, http_url, service_desc=None, service_port=80):

        self.service_url = http_url
        super().__init__(service_port, "http", service_desc)

    def get_status(self, headers=None, params=None):

        try:
            service_response = requests.get(self.service_url, headers=headers, params=params)
        
        except requests.exceptions.ConnectionError as error_msg:

            return return_status(500, error_msg)
           
        else:

            return return_status(
                service_response.status_code,
                service_response.text
            )

    def get_response_time(self, headers=None, params=None):

        """service_response = self.get_status(headers=headers, params=params)

        if service_response["status_code"] == 200:

            response = requests.get(self.http_url, headers=headers, params=params)
        
            return return_status(200, response.elapsed.total_seconds)

        return service_response
        """
        response = requests.get(self.http_url, headers=headers, params=params)

        if response.status_code == 200:

            return return_status(200, response.elapsed.total_seconds())
        
        return return_status(500, 0)


class MonitorDBMS(MonitorService):

    def __init__(self, dbms_metadata, service_port, dbms_module_name="psycopg2", service_url=None, service_desc=None):

        self.dbms_module = importlib.import_module(dbms_module_name)
        if dbms_metadata:
            self.dbms_connection = self.dbms_module.connect(
                host=dbms_metadata["server"], database=dbms_metadata["database"],
                user=dbms_metadata["user"], password=dbms_metadata["password"]
            )

        super().__init__(service_port, "tcp", service_url=service_url, service_desc=service_desc)
    
    def get_status(self):

        try:
            with self.dbms_connection.cursor() as cursor:

                cursor.execute(
                    "SELECT 1 + 1"
                )
                
                result = cursor.fetchone()

                if result:

                    return return_status(200, "Database is Alive")
                    
                return return_status(404, "result not found")
                
        except self.dbms_module.InterfaceError as error_msg:

            return return_status(501, error_msg)
        
        except self.dbms_module.OperationalError as error_msg:

            return return_status(502, error_msg)


class MonitorPort(MonitorService):

    def __init__(self, ip_address, service_port, service_proto="tcp", service_desc=None):

        self.ip_address = ip_address
        super().__init__(service_port, service_proto, service_desc)
    
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
