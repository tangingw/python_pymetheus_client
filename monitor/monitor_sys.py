import psutil


class MonitorCPU:
    
    def __init__(self):

        self.cpu_percent_overall = psutil.cpu_percent(interval=1)
        self.cpu_percent_per_cpu = psutil.cpu_percent(interval=1, percpu=True)

    def get_cpu_data(self):

        return self.__dict__


class MonitorMemory:

    def __init__(self):

        self.virtual_memory_obj = psutil.virtual_memory()
        self.virtual_memory_dict = {
            "total": self.virtual_memory_obj.total,
            "available": self.virtual_memory_obj.available,
            "usage_percent": self.virtual_memory_obj.percent,
            "used": self.virtual_memory_obj.used
        }

    def get_memory_data(self):

        return self.virtual_memory_dict


class MonitorDisk:

    def __init__(self):

        self.all_disk_partition = psutil.disk_partitions(all=True)
    
    def get_all_partition(self):

        return [
            {
                "device": disk.device, "mount_point": disk.mountpoint,
                "fstype": disk.fstype, "opts": disk.opts
            } 
            for disk in self.all_disk_partition
        ]

    def get_disk_usage(self, path):

        try:
            disk_usage_info = psutil.disk_usage(path)
            return {
                "path": path,
                "total": disk_usage_info.total,
                "used": disk_usage_info.used,
                "free": disk_usage_info.free,
                "used_percentage": disk_usage_info.percent
            }

        except PermissionError:
            return {
                "path": path,
                "total": None,
                "used": None,
                "free": None,
                "used_percentage": None
            }

    def get_all_disk_usage(self):

        return [
            self.get_disk_usage(partition["mount_point"])
            for partition in self.get_all_partition()
        ]

    def get_disk_all_data(self):

        print(self.get_all_partition())
        return {
            partition["mount_point"]: {
                "partition": partition,
                "usage": self.get_disk_usage(
                    partition["mount_point"]
                )
            } 
            for partition in self.get_all_partition()
        }
