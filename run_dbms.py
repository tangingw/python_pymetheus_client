from monitor.monitor_service import MonitorDBMS

monitor_dbms = MonitorDBMS('5432', service_name="postgresql db")
monitor_dbms.connect_db(
    {
        "server": "192.168.0.179",
        "database": "postgres",
        "user": "postgres",
        "password": "tallgeese3"
    }
)
print(
    monitor_dbms.get_connection_count()
)

print(
    monitor_dbms.get_status()
)