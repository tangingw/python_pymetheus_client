from client.configuration import PyMetheusConfig
from client.baseclient import PyMetheusClient


class PyMetheusDeviceClient(PyMetheusClient):

    def __init__(self):

        self.load_config()
    
    def load_config(self, headers: dict=None):
        super().load_config(PyMetheusConfig(), headers=headers)

    def get_config(self):

        return self.config

    def write_config(self, config_data, filepath: str = None) -> dict:
        
        return super().write_config(PyMetheusConfig(), config_data, filepath=filepath)

    def get_data(self, parameters=None, data=None, json=None):

        return super().get_data(parameters=parameters, data=data, json=json)

    def put_data(self):
        return "PUT"
        #return super().put_data(data)

    def delete(self):
        return "DELETE"
        #return super().delete(data=data, json_data=json_data)
    
    def post_data(self, data=None):
        #return "POST"
        return super().post_data(data)
    
    def select_endpoint(self, endpoint_name):

        self.url = f"{self.url}/{endpoint_name}"

