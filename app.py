#
import json
import os
import shutil
import time

import watchdog.observers
import watchdog.events

class FileMoveRunner:
    def __init__(self, source_folder: str, target_folder: str) -> None:
        self.source_folder = source_folder
        self.target_folder = target_folder

    def move_file(self, source):
        shutil.move(source, self.target_folder)


class Monitor(watchdog.events.FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()
        self.on_created_callback = None

    def on_created(self, event: watchdog.events.FileSystemEvent):
        super().on_created(event)
        path = event.src_path
        name = os.path.basename(path)
        print('{}, CREATED'.format(name))
        self.on_created_callback(path)
        return 
    
    def on_deleted(self, event: watchdog.events.FileSystemEvent):
        return super().on_deleted(event)

    def on_modified(self, event: watchdog.events.FileSystemEvent):
        return super().on_modified(event)
    
    def on_moved(self, event: watchdog.events.FileSystemEvent):
        return super().on_moved(event)

    def set_on_created_callback(self, callback: callable):
        self.on_created_callback = callback


CONFIG = './config.json'
SOURCE = ''
TARGET = ''

def load_config():
    global CONFIG, SOURCE, TARGET

    with open(CONFIG, 'r') as f:
        j = json.load(f)
        print('j:', j)

    SOURCE = j['source_dir']
    TARGET = j['target_dir']

if __name__ == "__main__":


    load_config()
    print('Src: {}, Target: {}'.format(SOURCE, TARGET))

    runner = FileMoveRunner(source_folder=SOURCE, target_folder=TARGET)

    event_handler = Monitor()
    event_handler.set_on_created_callback(runner.move_file)
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, SOURCE, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()