# Testing PR kube-demo

Prerequisites
Requires Ansible 1.2 or newer

Expects 4 ubuntu nodes (at least 16.04)

1 - Controller node from where you run automation to deploy kubernetes cluster and as well prometheus.

1 - Master

2 - Worker nodes (slaves)


Clone the repo on Controller node

And Run python demo-setup.py --all 

Help:
python demo-setup.py --help
usage: demo-setup.py [-h] [--log-level LOG_LEVEL]
                     [--kube | --resetkube | --prometheus | --all]

optional arguments:

  -h, --help            show this help message and exit
  
  --log-level LOG_LEVEL set the log level
  
  --kube                to deploy kubernetes cluster
  
  --resetkube           to reset kubernetes cluster
  
  --prometheus          to deploy prometheus cluster
  
  --all                 to deploy kubernetes and prometheus cluster


![alt text](https://github.com/hgolla-repos/kube-demo/blob/master/demo.PNG)

Prometheuse dashboard can be accessed through http://workernode1:30000 or http://workernode2:30000
