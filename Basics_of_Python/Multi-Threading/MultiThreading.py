# Thread:
# Thread in Python is a separate flow of execution. Threads allow a program to operate more efficiently by performing multiple operations concurrently within a process.
# Python provides the threading module to create and manage threads easily.
# Every execution will have the one thread that is Main Thread.
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):                  # Run method is the default method in the thread class and if we don't use the run method the code multi threading will not work
        for i in range(0,5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(0,5):
            print("Hi")
            sleep(1)

t1= Hello()
t2= Hi()

t1.start()
sleep(0.2)
t2.start()
# When you call start(), :
# It tells Python's threading system to create a new, separate thread and then calls the run() method within that new thread. This is how true multithreading works.
# If you call run() directly,
# it won't create a new thread. Instead, it will just execute the run() method like a regular function call within the same thread (typically the main thread).
t1.join()
t2.join()

# Why user Join():
# The .join() method in threading is used to wait for a thread to complete its execution.
# It blocks the calling thread (typically the main thread) until the thread on which .join() was called has finished running.

print("Bye")            # Print(Bye) is using the main thread.
