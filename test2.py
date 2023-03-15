#!/usr/bin/python

from converse import module
#from converse import formal_module
from converse.formal_module import greeting

name = input('Please enter your name: ')
print(f'{name}: Good evening package.')
module.hello(name)
print()

print(f'{name}: Can you be a bit more formal please?')
greeting(name)
