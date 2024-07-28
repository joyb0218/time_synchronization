import time
import random
import os

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Event number and descriptions
SYSTEM_EVENTS = {
    1: "User login",
    2: "User logout",
    3: "File created",
    4: "File deleted",
    5: "File modified",
    6: "Disk space low",
    7: "Network connection established",
    8: "Network connection lost",
    9: "Application started",
    10: "Application stopped",
    11: "Scheduled task executed",
    12: "Scheduled task failed",
    13: "Security policy updated",
    14: "Unauthorized access attempt",
    15: "System boot",
    16: "System shutdown",
    17: "CPU usage high",
    18: "Memory usage high",
    19: "Disk read/write error",
    20: "Hardware failure detected",
    21: "Software update available",
    22: "Software update installed",
    23: "User account created",
    24: "User account deleted",
    25: "Password change required",
    26: "Malware detected",
    27: "Backup completed successfully",
    28: "Backup failed",
    29: "Printer added",
    30: "Printer removed",
    31: "Print job started",
    32: "Print job completed",
    33: "System configuration changed",
    34: "Firewall rule added",
    35: "Firewall rule removed",
    36: "Remote desktop session started",
    37: "Remote desktop session ended",
    38: "Email sent",
    39: "Email received",
    40: "Database query executed",
    41: "Database connection established",
    42: "Database connection lost",
    43: "Web server started",
    44: "Web server stopped",
    45: "New device connected",
    46: "Device disconnected",
    47: "Service started",
    48: "Service stopped",
    49: "User role changed",
    50: "Log file rotated",
}

def generate_log(filename):
    with open(os.path.join(LOG_DIR, filename), "a") as log_file:
        while True:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            event_number = random.randint(1, 50)
            event_description = SYSTEM_EVENTS[event_number]
            log_message = f"{timestamp} - Event {event_number}: {event_description}"
            log_file.write(log_message + "\n")
            print(log_message)
            time.sleep(random.randint(1, 5))

if __name__ == "__main__":
    generate_log("system1.log")
