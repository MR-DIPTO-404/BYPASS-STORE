import os, sys
os.system('clear')
os.system('git pull')
try:
    __import__("SPYVIP").Spy()
except Exception as e:
    exit(str(e))
