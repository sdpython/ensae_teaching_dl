# -*- encoding: utf-8 -*-
"""
@file
@brief Around :epkg:`deep learning`.
"""

__version__ = "0.2.194"
__author__ = "Xavier Dupré"


def check(log=False):
    """
    Checks the library is working.
    It raises an exception.
    If you want to disable the logs:

    @param      log     if True, display information, otherwise
    @return             0 or exception
    """
    return True


def _setup_hook(use_print=False):
    """
    If this function is added to the module,
    the help automation and unit tests call it first before
    anything goes on as an initialization step.
    """
    if use_print:
        print("Success: _setup_hook")
