import os
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ClicksConversionsHandler(FileSystemEventHandler):
    def __init__(self, process_function):
        self.process_function = process_function

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.csv'):
            self.process_function(event.src_path)

def process_clicks_conversions(file_path):
    df = pd.read_csv(file_path)
    # Add further processing as needed
    print(f"Processed clicks/conversions file: {file_path}")

if __name__ == "__main__":
    path = "path/to/clicks_conversions/"
    event_handler = ClicksConversionsHandler(process_clicks_conversions)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
