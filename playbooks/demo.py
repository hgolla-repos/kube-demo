#!/usr/bin/env python


import atexit
import collections
import getpass
import logging
import os
import readline
import sys
import types
import paramiko

import requests
from requests.auth import HTTPBasicAuth
import yaml

from collections import OrderedDict


log_levels = {
    'critical': logging.CRITICAL,
    'debug':    logging.DEBUG,
    'error':    logging.ERROR,
    'warning':  logging.WARNING,
    'info':     logging.INFO,
}

# Just echo that we are done
def done():
    print 'setup is complete'
    return True



