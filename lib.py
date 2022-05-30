import sys

def success(text):
    print('\033[92m'+text+'\033[0m')
def warning(text):
    print('\033[93m'+text+'\033[0m')
def fail(text):
    sys.exit('\033[91m'+text+'\033[0m')