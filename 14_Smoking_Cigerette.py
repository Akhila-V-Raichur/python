import threading as th
import random
import time

def generateRandomItems():
    items = random.sample([0,1,2], 2)
    return items

class cigaretteSmoker:
    def __init__(s, rounds):
        s.condMutex = th.Condition()
        s.vendorSleep = th.Semaphore(0)
        s.rounds = rounds
        s.ingredients = ['TOBACCO', 'PAPER', 'MATCHES']

        # No item is available on table.
        s.availableItems = [False, False, False]
        s.smokerThreads = []
        s.terminate = False

        # Create three smokers threads.
        s.smokerThreads.append(th.Thread(target=s.smokerRoutine, \
                                  name='Smoker with Tobacco', args=(1, 2)))
        s.smokerThreads.append(th.Thread(target=s.smokerRoutine, \
                                  name='Smoker with Paper', args=(0, 2)))
        s.smokerThreads.append(th.Thread(target=s.smokerRoutine, \
                                  name='Smoker with Matches', args=(0, 1)))
        for smokers in s.smokerThreads:
            smokers.start()

        # Create vendor thread.
        s.vendorThread = th.Thread(target=s.vendorRoutine)
        s.vendorThread.start()

    def vendorRoutine(s):
        for i in range(s.rounds):

            # Generate two random items.
            randomItems = generateRandomItems()
            s.condMutex.acquire()
            print('\nVendor produced: {0} and {1}'.\
                  format(s.ingredients[randomItems[0]], \
                         s.ingredients[randomItems[1]]))

            # Make items available on table.
            s.availableItems[randomItems[0]] = True
            s.availableItems[randomItems[1]] = True

            # Announce to all smokers that items are made available on table.
            s.condMutex.notify_all()
            s.condMutex.release()

            # Go to sleep till the selected smoker is done with smoking.
            s.vendorSleep.acquire()

    def smokerRoutine(s, neededItem1, neededItem2):
        myName = th.current_thread().name
        while (True):
            s.condMutex.acquire()

            # Block till the needed items are on table.
            while (False == s.availableItems[neededItem1] or
                   False == s.availableItems[neededItem2]):
                s.condMutex.wait()
            s.condMutex.release()

            # Check if it was a terminate signal.
            if (True == s.terminate):
                break

            # Pickup the items from the table.
            s.availableItems[neededItem1] = False
            s.availableItems[neededItem2] = False

            # All ingredients are with you start smoking.
            print('{0} started smoking.'.format(myName))
            s.startUnhealthyActSmoking()
            print('{0} ended smoking.'.format(myName))

            # Smoking is done, wakeup the sleeping vendor.
            s.vendorSleep.release()

    def startUnhealthyActSmoking(s):
        randomTime = random.randint(1,100)
        randomTime %= 5
        time.sleep(randomTime+1)

    def waitForCompletion(s):

        # Wait for vendor thread to end.
        s.vendorThread.join()

        # Send terminate signal to smoker threads.
        s.condMutex.acquire()
        s.terminate = True
        s.availableItems = [True, True, True]
        s.condMutex.notify_all()
        s.condMutex.release()

Chances=5
obj = cigaretteSmoker(Chances)
obj.waitForCompletion()