import os, sys
os.system('clear')
os.system('git pull')
try:
    __import__("SPY").file()
except Exception as e:
    exit(str(e))
