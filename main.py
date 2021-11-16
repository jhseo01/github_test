import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from watchdog.events import FileSystemEventHandler
from shutil import copyfile


        
class GameListHandler1(PatternMatchingEventHandler):
    def __init__(self):
        PatternMatchingEventHandler.__init__(self, patterns=watchFilePatterns1, ignore_directories=True, case_sensitive=False)
        
    def on_created(self, event): #파일, 디렉터리가 생성되면 실행
        print(event.src_path)
            
class GameListHandler(PatternMatchingEventHandler):
    def __init__(self):
        PatternMatchingEventHandler.__init__(self, patterns=watchFilePatterns, ignore_directories=True, case_sensitive=False)

    def on_modified(self, event):
        ##destFile = backupDir  + event.src_path[event.src_path.index('/roms/'):]
        ##Backup(event.src_path, destFile)
        print("modified")
        f = open("C:/J/file_path.txt", 'rt', encoding='UTF8')
        line = f.readline()
        print(line)
        f.close()


if __name__ == "__main__":
    watchPath1 = 'C:\J'
    watchFilePatterns1 = ['*CR_*.txt']
    watchPath = 'C:\J'
    watchFilePatterns = ['file_path.txt']
    #backupDir = '/home/pi/kimstar/backup'

    event_handler1 = GameListHandler1()
    observer1 = Observer()
    observer1.schedule(event_handler1, watchPath1, recursive=True)
    observer1.start()
    
    event_handler = GameListHandler()
    observer = Observer()
    observer.schedule(event_handler, watchPath, recursive=True)
    observer.start()
    

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
        observer1.stop()
        observer1.join()