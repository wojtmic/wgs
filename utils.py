import threading
import subprocess

def start_async(cmd: list):
    threading.Thread(target=subprocess.run, args=(cmd,)).start()