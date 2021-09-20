import platform


class MonitorPlatform:

    def __init__(self):

        self.platform_name = platform.system()
        self.python_version = platform.python_version()
    
    def get_platform_info(self):

        platform_uname_obj = platform.uname()
        platform_uname_dict = {
            "system": platform_uname_obj.system,
            "machine_name": platform_uname_obj.node,
            "release": platform_uname_obj.system,
            "version": platform_uname_obj.version,
            "architecture": platform_uname_obj.machine,
            "processor_type": platform_uname_obj.processor,
            "python_version": self.python_version
        }

        if self.platform_name == "Windows":

            platform_win_version = platform.win32_ver()
            platform_uname_dict.update(
                {
                    "windows_version": {
                        "release": platform_win_version[0],
                        "version": platform_win_version[1],
                        "csd": platform_win_version[2],
                        "ptype": platform_win_version[3]
                    }
                }
            )

        elif self.platform_name == "Darwin":
        
            platform_mac_version = platform.mac_ver()
            platform_uname_dict.update(
                {
                    "mac_version": {
                        "release": platform_mac_version[0],
                        "versioninfo": {
                            "version": platform_mac_version[1][0],
                            "dev_stage": platform_mac_version[1][1],
                            "non_release_version": platform_mac_version[1][2]
                        },
                        "machine": platform_mac_version[2]
                    }
                }
            )

        return platform_uname_dict

    def get_class_name(self):

        if self.__class__.__base__.__name__ != "object":

            return self.__class__.__name__
        
        return self.__class__.__base__.__name__