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


def test_get_network_ping(net_app):

    network_ping = net_app.get_ping()

    assert isinstance(network_ping, dict)
    assert "status" in network_ping.keys()
    assert "message" in network_ping.keys()

    assert network_ping["status"] in [200, 500]


def test_get_network_ping_target_ip(net_app):

    for target_ip in ["1.1.1.1", "192.168.200.1", "9.9.9.9"]:

        network_ping = net_app.get_ping(target_ip)

        assert isinstance(network_ping, dict)
        assert "status" in network_ping.keys()
        assert "message" in network_ping.keys()

        assert network_ping["status"] in [200, 500]

def test_get_network_io_counter(net_app):

    io_counter = net_app.get_net_io_counters()

    for _, interface_io in io_counter.items():

        assert isinstance(interface_io, dict)
        assert len(
            set(
                interface_io.keys()).intersection(
                    [
                        'bytes_sent', 'bytes_recv', 
                        'packets_sent', 'packers_recv', 
                        'errin', 'errout', 'dropin', 'dropout'
                    ]
                )
        ) == len(interface_io.keys())