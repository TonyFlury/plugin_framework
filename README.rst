Plugin Framework
================

The code in this repository accompanies the blog post `An Easy Plugin Framework <http://viewfromthekeyboard.blogspot.co.uk/2015/11/an-easy-to-use-extend-plugin-framework.html>`_

This code demonstrates a flexible plugin Framework using dynamic importation to implement (and potentially extend base functionality).

The framework consists of the ``pluginFramework.pluginFramework`` module. Within the module, there are two key classes.

- ``PluginBase`` is used by the framework to identify all potentially plugins. All classes which implement plugins must inherit from this class.
     ``pluginFramework.PluginBase()``

     Methods:
         The PluginBase method implements a single class method :

         -``PluginBase.register()``

         The base definition of register generates a NotImplementedError exception, and this method **must** be overriden by all classes
         which are plugins. This register method can have any functionality required by the application (including disabling base application functionality). All the framework requires is that this method exists, and will return.

- ``PluginFramework`` is used by the application to dynamically search for and import modules and classes which implement specified plugin functionality.


     -``pluginFramework.PluginFramework(<app_name>, <BaseClasses>)``
         - ``app_name`` : The name of the application - used to construct the path to the plugin directory
         - ``BaseClasses`` : A list/tuple of classes from which the plugins should inherit.


          This framework assumes that the application implements one or more classes which define the basic functionality and which can be augmented via plugins. These are the BaseClasses. The classes implemented in the plugin modules should inherit from one of these BaseClasses, as well PluginBase.

     Methods :
        The PluginFramework class implements a single method :

        - ``PluginFramework.bycategory(BaseClass)``

          This method iterates across all the classes defined in the plugin, and returns those which inherit BaseClass. The iterator returns a tuple of the class, and the registration info return by the register method on this class.

This repository includes a dummy application (application.py & bases.py) which demonstrate a simple application using the PluginFramework, and simple example plugin.

When you run the application ``python application.py`` you will notice that the registration and name/workerType information are all correctly printed - even though the mines.py module is never explicitly imported.

The plugin framework will search for plugins in two places :

- <app_path>/plugins
- ~/.<app_name>/plugins

where app_path is the default path to the application executable/python script, and app_name is the friendly name of the application as passed to the PluginFramework when it is initialised.