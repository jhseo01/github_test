import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_WATCH = "./logDir"
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_WATCH, recursive=True)
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
    def on_moved(event):
        print("move 발생")

    def on_created(shelf,event):
       print("move 발생")

    def on_deleted(shelf,event):
        print("delete 발생")

    def on_modified(shelf,event):
        print("modified 발생")

    def on_any_event(shelf,event):
        print("특정 event 발생")

if __name__ == "__main__":
    w = Watcher()
    w.run()