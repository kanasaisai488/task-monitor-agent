
# main.py – TaskMonitorAgent Watcher (multi-project ready)

import os
import time
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from agent import diff_tracker

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, watch_path):
        self.watch_path = watch_path

    def on_modified(self, event):
        if event.is_directory: return
        print(f"📌 Change detected: {event.src_path}")
        # You can plug in diff_tracker or trigger pipeline here

def run_watcher(watch_path):
    print(f"👁️ Monitoring started on: {watch_path}")
    event_handler = FileChangeHandler(watch_path)
    observer = Observer()
    observer.schedule(event_handler, path=watch_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch-folder", help="Path to project folder to monitor", required=True)
    args = parser.parse_args()

    folder = os.path.abspath(args.watch_folder)
    if not os.path.exists(folder):
        print(f"❌ Folder does not exist: {folder}")
    else:
        run_watcher(folder)
