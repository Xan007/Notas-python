import logging 
import sys

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
    with open('file.log') as file:
        read_data = file.read()
except Exception as ex:
    print(ex)
    logging.exception("Atrape un error") #########