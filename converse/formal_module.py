#!/usr/bin/python

from converse import get_name


def greeting(name):
    print(f'{get_name(__name__)}: Enchanté {name}')


if __name__ == '__main__':
    greeting('I get the sense that I\'m talking to myself')
