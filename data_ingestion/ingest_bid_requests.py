import os
import fastavro
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class BidRequestsHandler(FileSystemEventHandler):
    def __init__(self, process_function):
        self.process_function = process_function

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.avro'):
            self.process_function(event.src_path)

def process_bid_requests(file_path):
    with open(file_path, 'rb') as f:
        reader = fastavro.reader(f)
        for record in reader:
            # Add further processing as needed
            print(record)
    print(f"Processed bid requests file: {file_path}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    path = "path/to/bid_requests/"
    event_handler = BidRequestsHandler(process_bid_requests)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
