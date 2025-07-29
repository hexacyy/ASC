import time
import os
from detector import analyze_command
from alerter import send_alert
from logger import log_alert

# Path to the simulated live command log
LOG_SOURCE = "live_commands.log"

# Function: Continuously watches the live_commands.log file for new entries
def monitor_file():
    print(f"Monitoring {LOG_SOURCE} for new commands...\n")

    # Secure Coding: Ensure the log source file exists before reading
    if not os.path.exists(LOG_SOURCE):
        raise FileNotFoundError(f"[SECURITY] Required log file not found: {LOG_SOURCE}")

    # Open the file in read mode and jump to the end
    with open(LOG_SOURCE, "r") as f:
        f.seek(0, 2)  # Move to end of file for tail-like behavior

        while True:
            # Read new lines one at a time
            line = f.readline()

            if not line:
                time.sleep(1)  # Pause briefly to avoid CPU overuse
                continue

            cmd = line.strip()
            if not cmd:
                continue

            # Analyze the new command
            result = analyze_command(cmd)

            print(f">> {cmd}")
            print(f"[Verdict] {result['verdict'].upper()} | [Reason] {result['reason']}\n")

            # Log and alert if command is not safe
            if result['verdict'] != "legitimate":
                send_alert(cmd, result)
                log_alert(cmd, result)

# Entry point to start monitoring
if __name__ == "__main__":
    monitor_file()
