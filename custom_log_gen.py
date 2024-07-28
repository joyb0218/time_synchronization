import logging
import os
from datetime import datetime, timedelta
import win32evtlog
import pywintypes

# Set up logging to overwrite the log file each time the script runs
log_file_path = os.path.join(os.path.dirname(__file__), 'application_events_last_hour.log')
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def get_recent_events(hours=1):
    server = 'localhost'
    log_type = 'Application'
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    hand = win32evtlog.OpenEventLog(server, log_type)
    now = datetime.now()
    threshold_time = now - timedelta(hours=hours)

    events = []
    while True:
        events_chunk = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events_chunk:
            break
        for event in events_chunk:
            try:
                event_time = datetime.fromtimestamp(event.TimeGenerated.timestamp())
                if event_time >= threshold_time:
                    events.append(event)
                else:
                    # Stop processing if we have reached events older than the threshold
                    win32evtlog.CloseEventLog(hand)
                    return events
            except Exception as e:
                logging.error(f"Error processing event: {e}")
                continue

    win32evtlog.CloseEventLog(hand)
    return events

def log_events_to_file(events):
    with open(log_file_path, 'w') as file:
        for event in events:
            try:
                event_time = datetime.fromtimestamp(event.TimeGenerated.timestamp()).strftime('%Y-%m-%d %H:%M:%S')
                event_id = event.EventID & 0xFFFF  # Masking to get the correct Event ID
                event_type = event.EventType
                event_category = event.EventCategory
                event_source = event.SourceName
                event_message = ''.join(event.StringInserts) if event.StringInserts else ''

                file.write(f"Time: {event_time}, ID: {event_id}, Type: {event_type}, Category: {event_category}, Source: {event_source}, Message: {event_message}\n")
            except Exception as e:
                logging.error(f"Error writing event to file: {e}")

def main():
    logging.info("Script started")
    try:
        events = get_recent_events(hours=1)
        if events:
            log_events_to_file(events)
            logging.info(f"Logged {len(events)} events to {log_file_path}")
        else:
            logging.info("No events found in the last hour")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Script finished")

if __name__ == "__main__":
    main()
