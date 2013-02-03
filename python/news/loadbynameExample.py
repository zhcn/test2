from engines import *
import importlib

a = Engine()
a.func()

module = __import__('engines')
b = getattr(module,'Engine')()

b.func()
