# k8s-deploy
The repository contains scripts and settings files for kubernetes, which build app (flask, php) and install it in a minikube cluster.   

### minikube
Firstly install minikube https://minikube.sigs.k8s.io/docs/start/
then start it
```shell
minikube start
kubectl get po -A
minikube dashboard
```

### manual deploy
For deploy app manually 
```shell
kubectl create deployment app --image=yaburov/flask-app:1
kubectl expose deployment app --type=NodePort --port=5000
```

Then to check
```shell
kubectl get services hello-minikube
```
and
```shell
minikube service hello-minikube
```
for forwarding
```shell
kubectl port-forward service/app 8080:5000
```

### script deploy

### redeploy

## Links
* kubernetes docs https://kubernetes.io/ru/docs/home/
* Azure Cloud https://portal.azure.com/?quickstart=true#blade/Microsoft_Azure_Resources/QuickstartCenterBlade  27.11.2021

## Next TO DO
* deploy to another cluster
