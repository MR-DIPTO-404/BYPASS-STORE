import os, sys
os.system('clear')
try:
    __import__("SPYVIP").Spy()
except Exception as e:
    exit(str(e))
