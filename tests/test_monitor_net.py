import pytest
import random
from monitor.monitor_net import MonitorNetwork


@pytest.fixture
def net_app():

    random.seed()
    return MonitorNetwork()


def test_get_network_interface(net_app):

    network_interfaces = net_app.get_network_interface()
    assert isinstance(network_interfaces, dict)
    
    network_interfaces_list = list(network_interfaces.keys())
    random_network_interface = network_interfaces_list[
        random.randint(0, len(network_interfaces_list) - 1)
    ]

    assert isinstance(network_interfaces[random_network_interface], list)

    for interface in network_interfaces[random_network_interface]:

        assert isinstance(interface, dict)
        assert len(
            set(
                interface
            ).intersection(
                ["ip_type", "mac_address", "ip_address", "netmask", "broadcast"]
            )
        ) == len(interface.keys())


def test_get_network_connection(net_app):

    network_connection = net_app.get_connection_process()
    assert isinstance(network_connection, list)
    assert isinstance(network_connection[0], dict)

    for connection in network_connection:
        assert isinstance(connection, dict)
        assert len(
            set(connection.keys()).intersection(
                set(
                    [
                        "process_name", "status", "started_at",
                        "local_address", "remote_address", "protocol"
                    ]
                )
            )
        ) == len(connection.keys())


def test_get_all_info(net_app):

    network_info = net_app.get_all_info()

    assert isinstance(network_info, dict)
    assert "network_interfaces" in network_info.keys()
    assert "network_netstats" in network_info.keys()