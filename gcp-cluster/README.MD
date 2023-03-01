# GCP K8S

### kubectl common commands
```shell
kubectl get pods
kubectl get nodes
```

### work with pods 

#### deploy manually 
```shell
kubectl run app --image=yaburov/flask-app:1 --port=80 
kubectl delete pod app
```
#### deploy by yaml-configs 
```shell
kubectl apply -f pod.yml
kubectl delete -f pod.yml
```

#### work with it
```shell
kubectl describe pods app
kubectl exec app -- date
kubectl exec -it app -- sh
kubectl logs app
kubectl port-forward app 8080:80
```