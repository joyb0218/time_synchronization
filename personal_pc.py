import wmi
import time
import os

LOG_DIR = "../logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def log_system_events(filename):
    c = wmi.WMI()
    with open(os.path.join(LOG_DIR, filename), "a") as log_file:
        while True:
            for process in c.Win32_Process(["Caption", "CommandLine", "CreationDate"]):
                timestamp = process.CreationDate
                event_description = f"Process created: {process.Caption} {process.CommandLine}"
                log_message = f"{timestamp} - {event_description}"
                log_file.write(log_message + "\n")
                print(log_message)
            time.sleep(5)  # Check for new events every 5 seconds

if __name__ == "__main__":
    log_system_events("my_system.log")
