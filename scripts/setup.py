#!/usr/bin/env python


import atexit
import logging
import os
import sys

import requests
from requests.auth import HTTPBasicAuth

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
    print 'resetting kubernetes'
    d = os.path.dirname(os.getcwd())
    successful = os.system("sh " + os.getcwd() + "/scripts/kube-reset.sh " + d) == 0
def deploy_prometheus():
    print 'Deploying prometheus'
    d = os.path.dirname(os.getcwd())
    successful = os.system("sh " + os.getcwd() + "/scripts/deploy-prometheus.sh " + d) == 0
