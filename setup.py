from setuptools import setup, find_packages  

setup(name = 'scrapy-module_demo', 
   entry_points = { 
      'scrapy.commands': [ 
         'cmd_demo = my_module.commands:CmdDemo', 
      ], 
   }, 
)
