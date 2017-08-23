"""
Author: Ben Bornholm
Date: 8-22-17
Description:
https://www.shanelynn.ie/using-python-threading-for-multiple-results-queue/
"""
from notifications import slack_notification, email_notification
from watchdog_watcher import Watcher, q
from datetime import datetime
from threading import Thread
import logging
import yara


def load_yara_rules():
    import os
    tempDict = {}
    for root, dirnames, filenames in os.walk("yara_rules"):
        for filename in filenames:
            tempDict[filename]=(os.path.join(root, filename))
            print os.path.join(root, filename)

    return yara.compile(filepaths=tempDict)

def yara_rule_scan(rules, current_file):
    from os import path
    print "Current file {}".format(current_file)
    try:
        with open(current_file, 'rb') as f:
            matches = rules.match(data=f.read())
            print matches
            temp = "{} : {} : {}".format(str(datetime.now()),path.basename(current_file),matches)
            slack_notification(temp)
    except:
        logging.error("Error with loading file")

def main():
    # Load and compile YARA rules
    rules = load_yara_rules()

    # max number of threads
    num_threads = 5

    # Create watcher for directory and create thread
    w = Watcher()
    watchdog_worker = Thread(target=w.run)
    watchdog_worker.start()

    # Array of current worker threads
    workers = []

    # Loop until interupted
    try:
        while True:
            if not q.empty() and len(workers) < num_threads:
                # Get next queue item
                cur_task = q.get()
                print "Current task: {}".format(cur_task)

                # Create thread with next item
                num_threads += 1
                worker = Thread(target=yara_rule_scan, args=(rules,cur_task))
                worker.daemon=True
                workers.append(worker)
                worker.start()

                for t in workers:
                    if not t.isAlive():
                        workers.remove(t)
                        
    except KeyboardInterrupt:
        for t in workers:
            t.shutdown_flag.set()
        raise
main()
