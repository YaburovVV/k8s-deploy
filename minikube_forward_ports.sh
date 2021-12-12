#!/usr/bin/env bash
kubectl port-forward service/gagarin 8080:5000
#kubectl rollout restart deployment gagarin-new