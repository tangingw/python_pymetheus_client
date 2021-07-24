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

        self.config = json.loads(configuration.load_config())

        if self.config["status_code"] == 200:
        
            self.url = self.config["config"]["url"]    

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
