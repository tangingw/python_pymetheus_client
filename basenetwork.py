import sys
import re
import json
from utils import get_response
from abc import abstractmethod, ABC
from monitor.monitor_sys import MonitorCPU
from configuration import PyMetheusConfig


class PyMetheusClient(ABC):
    
    config = None
    headers = None
    url = None

    @abstractmethod
    def load_config(self, configuration, headers:dict = None):

        self.headers = {
            "Content-Type": "application/json"
        }

        if headers:

            self.headers.update(headers)

        self.config = configuration

        self.url = json.loads(self.config.load_config())["config"]["url"]    

    @abstractmethod
    def get_data(self, parameters=None, data=None, json=None):

        return get_response(
            self.url, headers=self.headers, method="GET", 
            params=parameters, data=data, json=json
        )

    @abstractmethod
    def post_data(self, data):

        return get_response(
            self.url,
            headers=self.headers, method="POST",
            json=data 
       )
    
    @abstractmethod
    def put_data(self, data):

        return get_response(
            self.url,
            headers=self.headers, method="PUT",
            json=data 
       )
    
    @abstractmethod
    def delete(self, parameters=None, json_data=None):

        return get_response(
            self.url,
            headers=self.headers, method="DELETE",
            params=parameters,
            json=json_data
        )


class PyMetheusDevice(PyMetheusClient):

    def __init__(self, configuration):

        self.load_config(configuration)
    
    def load_config(self, configuration, headers: dict=None):
        super().load_config(configuration, headers=headers)

    def get_data(self):
        return "Get"
        #return super().get_data(parameters=parameters, data=data, json=json)

    def put_data(self):
        return "Put"
        #return super().put_data(data)

    def delete(self):
        return "Delete"
        #return super().delete(data=data, json_data=json_data)
    
    def post_data(self, data=None):
        return "Post"
        #return super().post_data(data)


#c = PyMetheusConfig()
#m = PyMetheusDevice(c)
#print(m.get_data())