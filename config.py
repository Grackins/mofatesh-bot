import os

DATA_DIR = './data/'
COURSES_DIR = os.path.join(DATA_DIR, 'courses')
LISTENERS_DIR = os.path.join(DATA_DIR, 'listeners')

BOT_TOKEN = '1687090378:AAEEsA5nUI7gttTv6udi-xmomJkeI0B2JUc'

BOT_SLEEP_TIME = 10
COLLECTOR_SLEEP_TIME = 60

try:
    from local_config import *
except:
    pass
