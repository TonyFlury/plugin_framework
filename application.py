#!/usr/bin/env python
"""
# plugin_framework : Implementation of application

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

from pluginFramework import pluginFramework
import bases


class Application(object):
    def __init__(self):
        plugins = pluginFramework.PluginFramework("Our Game", (bases.Building,bases.Worker))
        for cls, info in plugins.bycategory(bases.Building):
            print "{}; Info - '{}', Name - '{}'".format(cls, info, cls.name())

        for cls, info in plugins.bycategory(bases.Worker):
            print "{}; Info - '{}', workerType - '{}'".format(cls, info, cls.workerType())

if __name__ == "__main__":
    app = Application()