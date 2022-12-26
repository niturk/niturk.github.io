import os
import time

from nb2hugo.writer import HugoWriter
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

writer = HugoWriter()
base_path = os.path.dirname(os.path.abspath(__file__))

class Watcher:
    DIRECTORY_TO_WATCH = base_path + '/notebooks'

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
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            try:
                writer.convert(event.src_path, base_path, 'posts')
            except Exception as e:
                print(e)
            print("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()