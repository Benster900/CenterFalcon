"""
Author: Ben Bornholm
Date: 8-22-17
Description:
https://www.shanelynn.ie/using-python-threading-for-multiple-results-queue/
"""
from notifications import slack_notification, email_notification
from watchdog_watcher import Watcher, q
import yara
from threading import Thread
import logging

def load_yara_rules():
    return yara.compile('yara_rules/RANSOM_MS17-010_Wannacrypt.yar')

def yara_rule_scan(rules, worker):
    print "working on rule"
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

    # max number of threads
    num_threads = 5

    # Create watcher for directory and create thread
    w = Watcher()
    #w.run()
    watchdog_worker = Thread(target=w.run)
    watchdog_worker.start()

    # Array of current worker threads
    workers = []

    # Loop until interupted
    while True:
        if not q.empty() and len(workers) < num_threads:
            # Get next queue item
            cur_task = q.get()

            # Create thread with next item
            worker = Thread(target=yara_rule_scan, args=(rules,cur_task))
            worker.start()
            workers.append(worker)

"""
##    # Run application till the end of time
##    while True:
##        print "hello"
##        # Do nothing as long as queue is empty
##        while not q.empty():
##            for i in range(num_theads):
##                # Get next queue item
##                cur_task = q.get()
                logging.debug('Start thread ', i)

                # Create thread with next item
                worker = Thread(target=yara_rule_scan, args=(rules,cur_task))
                worker.SetDaemon(True)

                # Start next thread
                worker.start()

                # Remove item from queue
                q.task_done


    # wait until the queue has been processed
    q.join()
"""
main()
