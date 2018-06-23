#!/usr/bin/env bash

echo "Invoking kubernetes deploy ansible playbook"

ansible-playbook -i playbooks/hosts playbooks/site.yml

eval "scp ubuntu@master:/home/ubuntu/.kube/config ~/.kube/config"
