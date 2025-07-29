
import time
from threading import Thread
from monitor import monitor_file

def test_monitor_alert_logs():
    open("live_commands.log", "w").close()
    open("logs/alerts.log", "w").close()

    t = Thread(target=monitor_file, daemon=True)
    t.start()

    with open("live_commands.log", "a") as f:
        f.write("powershell -enc aGVsbG8=\n")

    time.sleep(2)

    with open("logs/alerts.log", "r") as f:
        logs = f.read()
        assert "MALICIOUS" in logs
        assert "powershell -enc" in logs
