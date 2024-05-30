import os
import json
import logging
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class AdImpressionHandler(FileSystemEventHandler):
    def __init__(self, process_function):
        self.process_function = process_function

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.json'):
            self.process_function(event.src_path)

def process_ad_impression(file_path):
    with open(file_path) as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    # Add further processing as needed
    print(f"Processed ad impression file: {file_path}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    path = "path/to/ad_impressions/"
    event_handler = AdImpressionHandler(process_ad_impression)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
