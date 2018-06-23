#!/usr/bin/env bash

kubectl create -f clusterRole.yaml

NAMESPACE=${NAMESPACE:-monitoring}
KUBECTL="kubectl --namespace=\"${NAMESPACE}\""
eval "kubectl  create namespace \"${NAMESPACE}\""
eval "kubectl create -f clusterRole.yaml"
eval "${KUBECTL}  create -f config-map.yaml"

eval "${KUBECTL}  create -f prometheus-deployment.yaml"

eval "${KUBECTL}  create -f prometheus-service.yaml"

