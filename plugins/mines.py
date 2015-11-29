#!/usr/bin/env python
"""
# plugin_framework : Implementation of mines.py

Summary : 
    <summary of module/class being implemented>
Use Case : 
    As a <actor> I want <outcome> So that <justification>

Testable Statements :
    Can I <Boolean statement>
    ....
"""

from pluginFramework import pluginFramework
import application
import bases

__version__ = "0.1"
__author__ = 'Tony Flury : anthony.flury@btinternet.com'
__created__ = '29 Nov 2015'

class Mine(pluginFramework.PluginBase, bases.Building):
    """Doesn't implement the register method, so wont be used as a plugin"""
    pass


class GoldMine(Mine):
    @classmethod
    def register(cls_):
        return "Gold mine - place on a gold deposit"

    @classmethod
    def name(cls_):
        return "Basic Gold Mine"


class SilverMine(Mine):
    @classmethod
    def register(cls_):
        return "Silver mine - place on a silver deposit"

    @classmethod
    def name(cls_):
        return "Basic Silver Mine"


class GoldMiner(pluginFramework.PluginBase, bases.Worker):
    @classmethod
    def register(cls_):
        return "Gold Miner - feed with fish and beer to keep him working"

    @classmethod
    def workerType(cls_):
        return "Basic Gold Miner"


class SilverMiner(pluginFramework.PluginBase, bases.Worker):
    @classmethod
    def register(cls_):
        return "Silver Miner - feed with bread and meet to keep him working"

    @classmethod
    def workerType(cls_):
        return "Basic Silver Miner"
