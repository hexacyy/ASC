import os
from datetime import datetime

# Set path for the log file
LOG_FILE = "logs/alerts.log"

# Secure Coding: Ensure log directory exists to avoid file write errors
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Function: Logs alerts to alerts.log when a command is flagged
def log_alert(cmd, result):
    verdict = result.get("verdict", "unknown")
    reason = result.get("reason", "No reason provided")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Secure Coding: Truncate overly long commands to prevent log overflow or injection
    safe_cmd = cmd if len(cmd) <= 200 else cmd[:200] + "...[TRUNCATED]"

    # Format the log entry
    log_entry = f"[{timestamp}] [{verdict.upper()}] Command: {safe_cmd} | Reason: {reason}\n"

    # Secure Coding: Use safe file writing with 'with open' block to ensure file is properly closed
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
