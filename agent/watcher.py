# task_monitor_agent/agent/watcher.py

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, callback, watch_extensions=None):
        self.callback = callback
        self.watch_extensions = watch_extensions or [".py", ".yaml", ".md"]

    def on_modified(self, event):
        if not event.is_directory and self._is_valid_file(event.src_path):
            self.callback("modified", event.src_path)

    def on_created(self, event):
        if not event.is_directory and self._is_valid_file(event.src_path):
            self.callback("created", event.src_path)

    def _is_valid_file(self, path):
        return any(path.endswith(ext) for ext in self.watch_extensions)

class FileWatcher:
    def __init__(self, watch_paths, callback):
        self.watch_paths = watch_paths
        self.callback = callback
        self.observer = Observer()

    def start(self):
        event_handler = ChangeHandler(self.callback)
        for path in self.watch_paths:
            if os.path.exists(path):
                self.observer.schedule(event_handler, path, recursive=True)
        self.observer.start()
        print(f"[Watcher] Monitoring started on: {self.watch_paths}")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.observer.stop()
        self.observer.join()
        print("[Watcher] Monitoring stopped.")
