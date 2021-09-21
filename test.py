from register import RegisterDeviceHandler
from monitor.monitor_sys import MonitorDisk
from monitor.monitor_net import MonitorNetwork

device_handler = RegisterDeviceHandler()
print(
    device_handler.get_device()
)

"""


print(
    MonitorNetwork().get_network_interface()
)
"""