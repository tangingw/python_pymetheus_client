import pytest
from monitor.monitor_service import MonitorService
from monitor.monitor_service import MonitorPort
from monitor.monitor_service import MonitorHTTP


def test_monitor_service():

    dummy_service = MonitorService(1234, "tcp", "My Dummy Service")
    dummy_service_dict = dummy_service.get_service_metadata()

    assert isinstance(dummy_service_dict, dict)
    assert dummy_service_dict["service_port"] == 1234
    assert dummy_service_dict["service_desc"] == "My Dummy Service"
    assert dummy_service_dict["service_proto"] == "tcp"


def test_monitor_port_success():

    port_monitor = MonitorPort("192.168.0.183", "53", "udp", service_desc="My Own DNS")
    port_monitor_result = port_monitor.get_status()

    assert port_monitor_result["status_code"] == 200


def test_monitor_port_failed():

    port_monitor = MonitorPort("192.168.0.183", "52", service_desc="My Own DNS")
    port_monitor_result = port_monitor.get_status()

    assert port_monitor_result["status_code"] == 500


def test_monitor_http_success():

    http_monitor = MonitorHTTP("http://raspi3.mobieus.org:3333", service_desc="My Gitea server", service_port=3333)
    http_monitor_status = http_monitor.get_status()

    assert http_monitor_status["status_code"] == 200


def test_monitor_http_failed():

    http_monitor = MonitorHTTP("http://raspi3.mobieus.org:3334", service_desc="My Gitea server", service_port=3334)
    http_monitor_status = http_monitor.get_status()

    assert http_monitor_status["status_code"] == 500