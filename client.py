from configuration import PyMetheusConfig
from baseclient import PyMetheusClient


class PyMetheusDevice(PyMetheusClient):

    def __init__(self):

        self.load_config(PyMetheusConfig())
    
    def load_config(self, configuration, headers: dict=None):
        super().load_config(configuration, headers=headers)

    def get_data(self):
        #return "GET"
        parameters, data, json = None, None, None
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

