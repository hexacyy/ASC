# Function: Displays alert information to the console when a threat is detected
def send_alert(cmd, result):
    verdict = result.get("verdict", "unknown").upper()
    reason = result.get("reason", "No reason provided")

    # Secure Coding: Sanitize input to avoid terminal formatting issues or code injection in logs
    safe_cmd = cmd.replace("\n", " ").replace("\r", " ").strip()

    print("=== ALERT ===")
    print(f"[THREAT]  Detected a {verdict} command")
    print(f"[COMMAND] {safe_cmd}")
    print(f"[REASON]  {reason}")
    print("=============\n")
