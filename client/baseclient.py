import json
from utils import get_response
from abc import abstractmethod, ABC


class PyMetheusClient(ABC):
    
    config = None
    headers = None
    main_url = None
    url = None
    register_hash = None

    @abstractmethod
    def write_config(self, configuration, config_data, filepath: str = None) -> dict:

        return configuration.write_config(config_data, filepath=filepath)
    
    @abstractmethod
    def load_config(self, configuration, headers:dict = None, filepath: str = None):

        self.headers = {
            "Content-Type": "application/json"
        }

        if headers:

            self.headers.update(headers)

        self.config = json.loads(configuration.load_config(filepath=filepath))

        if self.config["status_code"] == 200:
        
            self.main_url = self.config["config"]["url"]
            self.url = self.config["config"]["url"]
            self.register_hash = self.config["config"].get("register_hash")

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
