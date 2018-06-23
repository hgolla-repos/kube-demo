#!/usr/bin/env python

import argparse
import requests
import logging
import os
from scripts import setup


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
    run_group.add_argument('--prometheus', dest='run_prometheus', action='store_true',
        help='to deploy prometheus cluster')
    args = parser.parse_args()
    if args.log_level != logging.INFO:
        ll = args.log_level.lower()
        if ll not in setup.log_levels:
            sys.exit('ERROR: Unsupported log level: ' + args.log_level)
        args.log_level = setup.log_levels[ll]
#    log = setup.getlogger(level=args.log_level)
#    log.info('setup called with args [{}]'.format(' '.join(sys.argv[1:])))
    if args.run_kube:
        print "deploy Kubernetes cluster"
        setup.deploy_kube()

    if args.reset_kube:
        print "reset Kubernetes cluster"
        setup.reset_kube()

    if args.run_prometheus:
        print "deploy prometheus cluster"
        setup.deploy_prometheus()
