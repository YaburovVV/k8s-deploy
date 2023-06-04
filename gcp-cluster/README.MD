# GCP K8S

## Pods
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
kubectl get pods -o wide 
```


## Deployment

### Manually run of deployment
```shell
kubectl get deployment
kubectl create deployment deploy-sample --image yaburov/php-sample:0.2
kubectl create deploy dp --image yaburov/flask-app:2
kubectl describe deployment deploy-sample
kubectl describe deployment pod deploy-sample-podname
kubectl scale deployment deploy-sample --replicas 4
kubectl get rs/replicaset
kubectl autoscale deployment deploy-sample --min 4 --max 6 --cpu-percent 80
kubectl get hpa
kubectl rollout history deployment/deploy-sample  
```


### Service for deploy
```shell
kubectl get services
kubectl get svc 
kubectl expose deployment deploy-sample --type=ClusterIP --port=80
kubectl delete service deploy-sample
kubectl expose deployment deploy-sample --type=NodePort --port=80
kubectl describe nodes | grep ExternalIP 
kubectl delete service deploy-sample
```

### Load balancer
```shell
kubectl expose deployment deploy-sample --type=LoadBalancer --port=80
kubectl get svc 
# http get ip:80 to shop service page 
kubectl delete service deploy-sample
```

- [x] e8 - pods
- [x] e9   
- [ ] e10
- [ ] e11
- [ ] e12