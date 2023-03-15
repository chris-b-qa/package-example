#!/usr/bin/python


def get_name(environment):
    return 'Module' if environment == '__main__' else 'Package'
