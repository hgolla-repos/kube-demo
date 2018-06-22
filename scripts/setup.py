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

def deploy_kube():
    print 'Deploying kubernetes'
    d = os.path.dirname(os.getcwd())
    successful = os.system("sh " + os.getcwd() + "/scripts/kube-setup.sh " + d) == 0
def reset_kube():
    print 'Deploying kubernetes'
    d = os.path.dirname(os.getcwd())
    successful = os.system("sh " + os.getcwd() + "/scripts/kube-reset.sh " + d) == 0
