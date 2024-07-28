import datetime

INGESTED_LOG = "ingested_logs.txt"


def analyze_logs():
    with open(INGESTED_LOG, "r") as log_file:
        logs = log_file.readlines()

    previous_timestamp = None
    for log in logs:
        timestamp_str = log.split(" - ")[0]
        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

        if previous_timestamp and timestamp < previous_timestamp:
            print(f"Time inconsistency detected: {timestamp} is earlier than {previous_timestamp}")

        previous_timestamp = timestamp

    print("Log analysis complete")


if __name__ == "__main__":
    analyze_logs()
