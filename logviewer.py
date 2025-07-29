import os

LOG_FILE = "logs/alerts.log"

def load_logs():
    if not os.path.exists(LOG_FILE):
        print("[!] No logs found.")
        return []

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    logs = []
    for line in lines:
        parts = line.strip().split("] ")
        if len(parts) >= 3:
            timestamp = parts[0].strip("[")
            verdict = parts[1].strip("[").lower()
            details = "] ".join(parts[2:])
            logs.append({
                "timestamp": timestamp,
                "verdict": verdict,
                "details": details
            })

    return logs

def filter_logs(logs, verdict_filter=None):
    if verdict_filter:
        logs = [log for log in logs if verdict_filter in log["verdict"]]
    return logs

def display_logs(logs):
    if not logs:
        print("[!] No logs to display.")
        return

    for log in logs:
        print("=" * 60)
        print(f"[Time]   {log['timestamp']}")
        print(f"[Verdict] {log['verdict'].upper()}")
        print(f"[Details] {log['details']}")
    print("=" * 60)
    print(f"[Total Alerts Shown: {len(logs)}]")

def main():
    logs = load_logs()

    verdict_filter = input("Filter by verdict? (malicious/suspicious/legitimate or leave blank): ").strip().lower()
    if verdict_filter not in ("malicious", "suspicious", "legitimate", ""):
        print("[!] Invalid filter. Showing all logs.")
        verdict_filter = None

    filtered_logs = filter_logs(logs, verdict_filter)
    display_logs(filtered_logs)

if __name__ == "__main__":
    main()
