# time_synchronization
This Python project will involve setting up a simulated logging environment where multiple systems generate logs with timestamps as a part of initiating security measures for a client and then moving into practicing on a personal computer.

# Steps:

1. Open PyCharm in elevated state (run as admin)
2. Create directory in PyCharm - file name: time_sync_log_analysis with subdirectory named: logs
3. Import ntplib, create NTP client to synchronize the system time - file name: ntp_client.py
4. Generate logs with timestamps - file name: log_generator.py
5. Ingest logs from different systems - file name: log_ingester.py
6. Analyze ingested logs for time consistency - file name: log_analyzer.py
7. Modify the NTP client to use NTPsec (if applicable) and implement basic security measures

# Security measures:

- Uses secure NTP configurations to prevent time spoofing and DDoS attacks.
- Implements monitoring and auditing to detect anomalies in time synchronization.

# Trouble Shooting:

ERROR 1: "A required privilege is not held by the client."<br>
SOLUTION: Run script in PowerShell or PyCharm from an elevated state (as admin)

ERROR 2. 'ingested_logs.txt' are empty.<br>
SOLUTION: Check if log is generating files. It was - stopped running and reran log ingester and analyzer script. Rec'v new txt file with logs.

# Mods:
- Decided to modify the log_generator.py file to give more information for the system events by renaming the original file with "_OLD", and then creating a new log_generator.py with enhanced script. Now generates file name: system1.log
- Changed timestamp in log_generator.py file to time.localtime() for all clients.
- Stepped out of the simulation and pip installed the wmi library to access the Windows Management Instrumentation (WMI) interface to query my own system events (created a new py file outside the log directory- file name: personal_pc.py (see project below)). Ended up switching from WMI to win32evtlog.

# time_synchronization for personal PC (not a simulation)

Moving out of the simulation of the NTP Client and into the system logs of my personal computer to synchronize time and analyze the logs for consistency using PyCharm.

# Steps:
- Created a personal log subdirectory under time_sync_log_analysis- named: logs_personal
- Created 2 new py files:
  - custom_log_gen.py: generates application events over the last hour
  - personal_pc.py: generates system files into the console directly (does not dump into a txt file). Does not timeout, be sure to stop running it when ready.
 
# Overview

By analyzing logs with accurate time stamps, the cyber security project aims to identify and prioritize potential threats, update security policies and procedures, and implement technical controls. This gives security teams the ability to identify anomalies, identify unauthorized access attempts, and signs of intrusions, as well as perform root cause analysis and forensic investigations. Python is an ideal tool for log analytics due to its versatility and rich ecosystem of libraries, such as pandas, numpy, and matplotlib, which facilitate data manipulation, analysis, and visualization. Its readable syntax allows for rapid development and easy maintenance of scripts, while its integration capabilities enable seamless connection with other tools and services.
