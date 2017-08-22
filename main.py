"""
Author: Ben Bornholm
Date: 8-22-17
Description:
https://www.shanelynn.ie/using-python-threading-for-multiple-results-queue/
"""
from watchdog_watcher import Watcher
from Queue import queue
import yara
import thread
import logging

def load_yara_rules():
    return yara.compile('yara_rules')

def yara_scanner(rules, worker):
    try:
        with open(work[1], 'rb') as f:
            matches = rules.match(data=f.read())
            if matches["matches"] == True:
                print matches["rule"]
            logging.info("{}".format(matches))
    except:
        logging.error("Error with loading file")

def main():
    # Load and compile YARA rules
    rules = load_yara_rules()

    # Create a queue
    q = Queue(maxsize=0)

    # max number of threads
    num_theads = 5

    # Create watcher for directory and create thread
    w = Watcher()
    #w.run()
    watchdog_worker = Thread(target=w.run)
    watchdog_worker.start()

    # Run application till the end of time
    while True:
        # Do nothing as long as queue is empty
        while not q.empty():
            for i in range(num_theads):
                # Get next queue item
                work = q.get()
                logging.debug('Start thread ', i)

                # Create thread with next item
                worker = Thread(target=yara_scanner, args=(rules,worker))
                worker.SetDaemon(True)

                # Start next thread
                worker.start()

                # Remove item from queue
                q.task_done


    # wait until the queue has been processed
    q.join()

main()
