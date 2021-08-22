from monitor.monitor_net import MonitorNetwork
from monitor.monitor_platform import MonitorPlatform
from monitor.monitor_sys import MonitorCPU
from monitor.monitor_sys import MonitorMemory
from monitor.monitor_sys import MonitorDisk

my_platform = MonitorPlatform()
my_cpu = MonitorCPU()
my_memory = MonitorMemory()
my_disk = MonitorDisk()
my_network = MonitorNetwork()
 
print(type(my_platform).__name__)
print(
    my_platform.get_platform_info()
)

print(
    my_cpu.get_cpu_data()
)

print(
    my_memory.get_memory_data()
)

print(
    my_disk.get_disk_all_data()
)

print(
    my_network.get_network_interface()
)
print(
    my_network.get_net_io_counters()
)