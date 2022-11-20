from os import wait
import time
import sys
import subprocess
import GetPairs as gp
import time

procs = []
    
url_list =  gp.get_url_list()

for url in url_list:
    proc =  subprocess.Popen([sys.executable, 'main.py', url])
    procs.append(proc)

for proc in procs:
    proc.wait()

