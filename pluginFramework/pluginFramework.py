#!/usr/bin/env python
"""
# plugin_framework : Implementation of pluginFramework.py

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

import os
import sys
import imp
import importlib
import inspect
import collections
import itertools


class PluginBase(object):
    @classmethod
    def register(cls_):
        """Must be implemented by the actual plugin class

           Must return a basic informational string about the plugin
        """
        raise NotImplementedError("Register method not implemented in {}".format(cls_))


class PluginFramework(object):
    def __init__(self, app_name, base_classes):
        self._app_name = app_name
        self._base_classes = base_classes
        self._dir_list = self._get_plugin_dirs()
        self._modules = self._identify_modules()
        self._classes = self._find_plugin_classes()
        self._bycategory = self._categorise_plugins()

    def _get_plugin_dirs( self ):
        """Return a list of pluginFramework directories for this application or user

        Add all possible pluginFramework paths to sys.path - these could be &lt;app_path&gt;/plugins and ~/&lt;app_name&gt;/plugins
        Only paths which exist are added to sys.path : It is entirely possible for nothing to be added.
        return the paths which were added to sys.path
        """
        # Construct the directories into a list
        plugindirs = [os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "plugins"),
                      os.path.expanduser("~/.{}/plugins".format(self._app_name))]

        # Remove any non-existant directories
        plugindirs =  [path for path in plugindirs if os.path.isdir(path)]

        sys.path = plugindirs + sys.path
        return plugindirs

    def _identify_modules(self):
        """Generate a list of valid modules or packages to be imported

        param: dir_list : A list of directories to search in
        return: A list of modules/package names which might be importable
        """
        # imp.get_suffixes returns a list of tuples : (&lt;suffix&gt;, &lt;mode&gt;, &lt;type&gt;)
        suff_list = [s[0] for s in imp.get_suffixes() if s[2] in [imp.PY_SOURCE, imp.PY_COMPILED]]

        # By using a set we easily remove duplicated names - e.g. file.py and file.pyc
        candidates = set()

        # Look through all the directories in the dir_list
        for dir in self._dir_list:
            # Get the content of each dir - don't need os.walk
            dir_content = os.listdir(dir)

            # Look through each name in the directory
            for file in dir_content:

                # Does the file have a valid suffix for a python file
                if os.path.isfile(os.path.join(dir,file)) and os.path.splitext(file)[1] in suff_list:
                    candidates.add(os.path.splitext(file)[0])

                # Is the file a package (i.e. a directory containing a __init__.py or __init__.pyc file
                if (os.path.isdir(os.path.join(dir, file)) and
                          any(os.path.exists(os.path.join(dir, file, f)) for f in ["__init__"+s for s in suff_list])):
                    candidates.add(os.path.splitext(file)[0])
        return candidates

    def _find_plugin_classes(self):
        """Return a list of classes which inherit from PluginBase

        param: module_list: a list of valid modules - from identify_modules
        return : A dictionary of classes, which inherit from PluginBase, and implement the register method
                The class is the key in the dictionary, and the value is the returned string from the register method
        """
        cls_dict = {}
        for mod_name in self._modules:
           m = importlib.import_module(mod_name)
           for name, cls_ in inspect.getmembers(m, inspect.isclass):
               if issubclass(cls_, PluginBase):
                  try:
                     info = cls_.register()
                  except NotImplementedError:
                      continue
                  else:
                      cls_dict[cls_] = info
        return cls_dict

    def _categorise_plugins(self):
        """Split the cls_dict into one or more lists depending on which
           base_class the pluginFramework class inherits from"""

        categorise = {}

        for base in self._base_classes:
            categorise[base] = {}
            for cls_ in self._classes:
                if issubclass(cls_,base):
                    categorise[base][cls_] = self._classes[cls_]
        return categorise

    def bycategory(self, base_class):
        for cls_, info in self._bycategory[base_class].iteritems():
            yield cls_, info