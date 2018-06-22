#!/usr/bin/env bash

echo "Invoking kubernetes deploy ansible playbook"

ansible-playbook -i playbooks/hosts playbooks/reset-cluster.yml
