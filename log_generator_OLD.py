import time
import random
import os

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def generate_log(filename):
    with open(os.path.join(LOG_DIR, filename), "a") as log_file:
        while True:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            log_message = f"{timestamp} - System event {random.randint(1, 100)}"
            log_file.write(log_message + "\n")
            print(log_message)
            time.sleep(random.randint(1, 5))

if __name__ == "__main__":
    generate_log("system1.log")
