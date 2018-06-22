#!/usr/bin/env python

import argparse
import atexit
import collections
import getpass
import logging
import os
import readline
import sys
import types
import paramiko
#sys.path.append('/home/hgolla/test/scripts')
from scripts import setup
import requests
from requests.auth import HTTPBasicAuth
import yaml


requests.packages.urllib3.disable_warnings()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--log-level', default=logging.INFO,
        help='set the log level')

    run_group = parser.add_mutually_exclusive_group()
    run_group.add_argument('--kube', dest='run_kube', action='store_true',
        help='to deploy kubernetes cluster')
    run_group.add_argument('--resetkube', dest='reset_kube', action='store_true',
        help='to deploy kubernetes cluster')
    args = parser.parse_args()
    if args.log_level != logging.INFO:
        ll = args.log_level.lower()
        if ll not in setup.log_levels:
            sys.exit('ERROR: Unsupported log level: ' + args.log_level)
        args.log_level = setup.log_levels[ll]
#    log = setup.getlogger(level=args.log_level)
#    log.info('setup called with args [{}]'.format(' '.join(sys.argv[1:])))
    if args.run_kube:
        print "Run Kube"
        setup.deploy_kube()

    if args.reset_kube:
        print "Run Kube"
        setup.reset_kube()
