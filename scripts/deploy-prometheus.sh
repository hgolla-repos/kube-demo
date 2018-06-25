#!/usr/bin/env bash


NAMESPACE=${NAMESPACE:-monitoring}
KUBECTL="kubectl --namespace=\"${NAMESPACE}\""
eval "kubectl  create namespace \"${NAMESPACE}\""
eval "kubectl create -f prometheus/clusterRole.yaml"
eval "${KUBECTL}  create -f prometheus/config-map.yaml"

eval "${KUBECTL}  create -f prometheus/prometheus-deployment.yaml"

eval "${KUBECTL}  create -f prometheus/prometheus-service.yaml"

