import pandas as pd
from detector import analyze_command
from alerter import send_alert
from logger import log_alert

# Function: Manual mode where user types one command at a time
def run_interactive_mode():
    print("=== MalCommandGuard (Manual Input Mode) ===")
    print("Type a command to simulate execution. Press Ctrl+C to exit.\n")

    while True:
        try:
            cmd = input(">> Command: ").strip()

            if not cmd:
                continue

            # Analyzes the typed command using detection engine
            result = analyze_command(cmd)

            print(f"[VERDICT] {result['verdict'].upper()}")
            print(f"[REASON] {result['reason']}\n")

            # Sends alert and logs if not legitimate
            if result['verdict'] != 'legitimate':
                send_alert(cmd, result)
                log_alert(cmd, result)

        except KeyboardInterrupt:
            print("\n[!] Exiting MalCommandGuard.")
            break

        # Secure Coding: Handles unexpected errors to avoid system crash
        except Exception as e:
            print(f"[ERROR] {str(e)}")


# Function: Reads a CSV of labeled commands to simulate scanning
def run_csv_simulation(csv_path):
    # Secure Coding: Drop rows with missing values to prevent exceptions
    df = pd.read_csv(csv_path).dropna(subset=["prompt", "Label"])
    print(f"Loaded {len(df)} commands from dataset...\n")

    for index, row in df.iterrows():
        cmd = row['prompt']
        actual = row['Label']

        # Run the detection engine on each command
        result = analyze_command(cmd)
        predicted = result['verdict']

        print(f">> {cmd}")
        print(f"[PREDICTED] {predicted.upper()} | [ACTUAL] {actual.upper()}")
        print(f"[REASON] {result['reason']}\n")

        if predicted != "legitimate":
            send_alert(cmd, result)
            log_alert(cmd, result)


# Entry point: decides which mode to run (CSV simulation or manual)
if __name__ == "__main__":
    import sys
    # Secure Coding: Checks for command-line argument presence to avoid index error
    if len(sys.argv) > 1 and sys.argv[1] == "csv":
        run_csv_simulation("data/cmd_huge_known_commented_updated.csv")
    else:
        run_interactive_mode()
