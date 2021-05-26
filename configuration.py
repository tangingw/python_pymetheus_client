from io import DEFAULT_BUFFER_SIZE
import os
import json


def _return_json(input_data: dict):

    return json.dumps(input_data)


class PyMetheusConfig:

    def __init___(self):

        self._config_data = None
    
    def load_config(self, filepath=None):

        default_path = "config/config.json"
        if filepath:

            default_path = filepath
        
        if os.path.exists(default_path):

            with open(default_path, "r") as config_file:

                self._config_data = json.loads(
                    config_file.read()
                )

            return _return_json(
                {
                    "status_code": 200,
                    "status_msg": "config loaded successfully.",
                    "config": self._config_data
                }
            )

        print("You do not have the configuration")
        return _return_json(
            {
                "status_code": 500,
                "status_msg": "config not found"
            }
        )

    def write_config(self, config_data: dict, filepath=None):

        default_path = "config/config.json"
        if filepath:

            default_path = filepath
        
        with open(default_path, "w", newline="", encoding="utf-8") as config_file:

            config_file.write(
                json.dumps(
                    config_data, indent=4, ensure_ascii=False
                )
            )

        return _return_json(
            {
                "status_code": 200,
                "status_msg": "config modified successfully."
            }
        )

    def read_config(self):

        return self._config_data