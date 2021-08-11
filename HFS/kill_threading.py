#!/usr/bin/python
# coding: UTF-8

import sys
import threading
try:
   import queue
except ImportError:
   import Queue as queue

class ExcThread(threading.Thread):

    def __init__(self, bucket):
        threading.Thread.__init__(self)
        self.bucket = bucket

    def run(self):
        try:
            raise Exception('An error occured here.')
        except Exception:
            self.bucket.put(sys.exc_info())


def main():
    bucket = queue.Queue()
    thread_obj = ExcThread(bucket)
    thread_obj.start()

    while True:
        try:
            exc = bucket.get(block=False)
        except Queue.Empty:
            pass
        else:
            exc_type, exc_obj, exc_trace = exc
            # deal with the exception
            print(exc_type, exc_obj)
            print(exc_trace)

        thread_obj.join(0.1)
        if thread_obj.is_alive():
            continue
        else:
            break


if __name__ == '__main__':
    main()