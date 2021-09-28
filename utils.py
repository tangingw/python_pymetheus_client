import json
import time
import threading
import requests
import urllib3
from queue import Queue


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def add_function_daemon(function_list,):

    my_queue = Queue()

    my_thread_list = [
        threading.Thread(
            target=my_func[0], args=(my_queue, my_func[1])
        ) 
        for my_func in function_list
    ]

    for my_thread in my_thread_list:

        my_thread.daemon = True
        my_thread.start()

    while True:

        try:

            time.sleep(1)

        except KeyboardInterrupt:

            print("Exiting")
            my_queue.put("e")
            exit(1)


def return_status(status_code, status_msg=None, status_value=None):

    return {
        "status_code": status_code,
        "status_msg": status_msg,
        "status_value": status_value
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
