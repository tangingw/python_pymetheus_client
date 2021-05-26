import sys
import re
from utils import get_response


class PyMetheusClient:
    
    def __init__(self, configuration, headers: dict = None):

        self.headers = {
            "Content-Type": "application/json"
        }

        if headers:

            self.headers.update(headers)

        self.config = configuration
        self.url = self.config.load_config()["config"]["url"]    

    def get_data(self, parameters=None, data=None, json=None):

        return get_response(
            self.url, headers=self.headers, method="GET", 
            params=parameters, data=data, json=json
        )

    def post_data(self, data):

        return get_response(
            self.url,
            headers=self.headers, method="POST",
            json=data 
       )
    
    def put_data(self, data):

        return get_response(
            self.url,
            headers=self.headers, method="PUT",
            json=data 
       )
    
    def delete(self, data=None, json_data=None):

        return get_response(
            self.url,
            headers=self.headers, method="DELETE",
            params=data,
            json=json_data
        )
