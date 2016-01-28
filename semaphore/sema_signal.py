# sema_signal.py
#
# An example of using a semaphore to signal

import threading
import time
from datetime import datetime

done = threading.Semaphore(0)
item = None

def producer():
    global item
    print "Producer: I produced a variable that should print the time this process started."
    print "Producer is going to sleep."
    item = datetime.now()
    time.sleep(10)
    #write data and release for consumer ot access
    print "Producer is alive. Signaling the consumer."
    # release so another thread can access the data
    done.release()

def consumer():
    print "I'm the consumer and I wait for data."
    print "Consumer is waiting."
    done.acquire()
    # acquire doesnt return until the parent process releases() the data
    print "This thread acquired data at: ", datetime.now()
    print "Time variable was produced at: ", item
    print "There should be a 10 second gap..."

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
