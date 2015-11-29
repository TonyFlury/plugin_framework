#!/usr/bin/env python
"""
# plugin_framework : Implementation of bases.py

Summary : 
    <summary of module/class being implemented>
Use Case : 
    As a <actor> I want <outcome> So that <justification>

Testable Statements :
    Can I <Boolean statement>
    ....
"""

__version__ = "0.1"
__author__ = 'Tony Flury : anthony.flury@btinternet.com'
__created__ = '29 Nov 2015'


class Building(object):
    """Dummy class to implement a building"""
    def build(self, x,y):
        pass

    def add_worker(self, worker):
        pass

    def get_produce(self):
        pass

class Worker(object):
    """Dummy class to implement a worker"""
    def create(self):
        pass

    def kill(self, x, y):
        pass

    def is_employed(self):
        pass