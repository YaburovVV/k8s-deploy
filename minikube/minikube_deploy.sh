#!/usr/bin/env bash
kubectl create deployment gagarin --image=gagarin:latest
kubectl expose deployment gagarin --type=NodePort --port=5000

#kubectl port-forward service/gagarin1 8080:5000