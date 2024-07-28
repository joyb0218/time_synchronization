import glob
import os

LOG_DIR = "logs"
INGESTED_LOG = "ingested_logs.txt"

def ingest_logs():
    with open(INGESTED_LOG, "w") as outfile:
        for log_file in glob.glob(os.path.join(LOG_DIR, "*.log")):
            with open(log_file, "r") as infile:
                outfile.write(infile.read())
    print(f"Logs ingested into {INGESTED_LOG}")

if __name__ == "__main__":
    ingest_logs()
