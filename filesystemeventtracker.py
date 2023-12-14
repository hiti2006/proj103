import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir ="C:/Users/HP/Downloads"
class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print("created!"+event.src_path+"has been created")
    def on_deleted(self,event):
        print("oops deleted!"_event.src_path+"has been deleted")
    def on_moved(self,event):
        print("moved"+event.src_path+"has been moved")
    def on_modified(self,event):
        print("modified"+event.src_path+"has been modified")
eventhandler=FileEventHandler()
observer=Observer()
observer.schedule(eventhandler,from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt :
    print("Stopped!")
    observer.stop()
