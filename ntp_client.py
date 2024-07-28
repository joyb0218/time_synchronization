import os
import time
import ntplib
from datetime import datetime


def set_system_time(ntp_time):
    # Format the NTP time for the system
    system_time = time.strftime('%m-%d-%Y %H:%M:%S', time.localtime(ntp_time))

    # Set the system time
    os.system(f'date {system_time.split()[0]}')
    os.system(f'time {system_time.split()[1]}')
    print(f"System time set to {system_time}")


def synchronize_time():
    try:
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request('pool.ntp.org')
        ntp_time = response.tx_time
        print(f"NTP time: {datetime.fromtimestamp(ntp_time)}")

        set_system_time(ntp_time)
    except Exception as e:
        print(f"Failed to synchronize time: {e}")


if __name__ == "__main__":
    synchronize_time()
