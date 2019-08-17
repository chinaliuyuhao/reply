#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
from threading import  Thread,Event
from queue import Queue
import time


q = Queue(10)
event = Event()
def worker(name):
    while q.qsize()<q.maxsize:
        if q.qsize()>0:
            event.set()
        print('{}正在生产产品'.format(name))
        time.sleep(1)
        q.put(1)
        print('产品已经生产完毕，剩余库存{}'.format(q.qsize()))
    else:
        print('货物已满,无法继续生产')


def consume(name):
    while event.wait():
        if q.qsize()>4:
            print('{}开始消费'.format(name))
            time.sleep(2)
            q.get()
            print('消费完毕')
        else:
            print('库存以不存在')
            event.clear()
