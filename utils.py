import json
import requests
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def return_status(status_code, status_msg):

    return {
        "status_code": status_code,
        "status_msg": status_msg
    }


def get_response(url, headers, method="GET", data=None, params=None, verify=False, json=None):

    response = requests.request(
        method, url, 
        headers=headers, 
        data=data, json=json,
        params=params, verify=verify
    )

    return {
        "status_code": response.status_code,
        "response_msg": response.json()
    }
