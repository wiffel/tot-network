"""This is a very much PoC it's 23:50 and I am very after whole work day promising your coax recruiter to finish test task today :( """
import time
import os
from pymongo import MongoClient

def init_db_client(host='localhost', port=27017):
    client = MongoClient(host, port)
    return client

def follow_from_last_line(_file):
    # Go to the end of the file
    _file.seek(0,2) 
    while True:
        line = _file.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        yield line
        # transfer to mongodb

if __name__ == "__main__":
    DEFAULT_LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'totaliatarian_network', 'access.log')
    LOG_FILE = os.environ.get('DJANGO_ACCESS_LOG_FILE', DEFAULT_LOG_FILE)
    db_client = init_db_client()
    ip_db = db_client['ip-db']
    ip_collection = ip_db['ips']
    
    with open(LOG_FILE, 'r') as log_file:
        last_line_watcher = follow_from_last_line(log_file)
        for line in last_line_watcher:
            ip_dict = {"ip": line}
            print('saved line' + line)
            ip_collection.insert_one(ip_dict)