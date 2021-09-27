import json
import time
import threading
import requests
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def add_function_daemon(function_list, wait_time=5):

    my_exit_signal = False

    while not my_exit_signal:

        try:

            my_thread_list = [
                threading.Thread(target=my_func, args=tuple()) for my_func in function_list
            ]

            for my_thread in my_thread_list:

                my_thread.daemon = True
                my_thread.start()

            time.sleep(wait_time)

        except KeyboardInterrupt:

            my_exit_signal = True
            for my_thread in my_thread_list:

                my_thread.join()

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
