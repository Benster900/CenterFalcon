"""
Author: Ben Bornholm
Date: 8-22-17
Description:
"""
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Queue import Queue
import time

# Create a queue
q = Queue(maxsize=0)

class Watcher:
    DIRECTORY_TO_WATCH = "/tmp/test"
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print "Error"

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            q.put(event.src_path)
            print "Received created event - %s." % event.src_path

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            q.put(event.src_path)
            print "Received modified event - %s." % event.src_path
