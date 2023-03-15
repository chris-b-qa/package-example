#!/usr/bin/python

from converse import get_name


def hello(name):
    print(f'{get_name(__name__)}: Yo {name}')


if __name__ == '__main__':
    hello('am I talking to myself?')
