
import sys
import os
from main import run_interactive_mode, run_csv_simulation
from monitor import monitor_file
from logviewer import display_logs, load_logs, filter_logs
from evaluate import run_evaluation

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_and_return():
    input("\n[Press Enter to return to the main menu...]")
    clear_screen()

def launcher_menu():
    while True:
        print("""
====== MalCommandGuard Launcher ======

1. Manual Mode (Type commands yourself)
2. CSV Replay Mode (Simulate from dataset)
3. Monitor Mode (Watch live_commands.log)
4. Evaluate Accuracy (Run evaluate.py)
5. View Log History
6. Exit
""")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_interactive_mode()
            pause_and_return()
        elif choice == "2":
            run_csv_simulation("data/cmd_huge_known_commented_updated.csv")
            pause_and_return()
        elif choice == "3":
            try:
                monitor_file()
            except KeyboardInterrupt:
                print("\n[!] Monitoring stopped by user.")
            pause_and_return()
        elif choice == "4":
            run_evaluation("data/cmd_huge_known_commented_updated.csv")
            pause_and_return()
        elif choice == "5":
            logs = load_logs()
            verdict = input("Filter by verdict (malicious/suspicious/legitimate) or leave blank: ").strip().lower()
            verdict = verdict if verdict in ["malicious", "suspicious", "legitimate"] else None
            filtered = filter_logs(logs, verdict)
            display_logs(filtered)
            pause_and_return()
        elif choice == "6":
            print("Exiting MalCommandGuard. Goodbye!")
            sys.exit(0)
        else:
            print("[!] Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    clear_screen()
    launcher_menu()
