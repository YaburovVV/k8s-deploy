# k8s-deploy
The repository contains scripts and settings giles for kubernetes, which create project (flask) and install it in a minikube cluster.   

### minikube
Firstly install minikube https://minikube.sigs.k8s.io/docs/start/
then start it
```shell
minikube start
kubectl get po -A
minikube dashboard
```

### flask app
Sample python app contains 2 files 
* api-server.py
* requirements.txt

#### for trying flask locally
```shell
python3 -m venv venv
source venv/bin/activate  
pip list
pip install -r requirements.txt   
export FLASK_APP=api-server  
python -m flask run --host=0.0.0.0 --port=80
deactivate
```

#### for trying docker locally
```shell
docker build -t flasktest .
docker run -it -p 80:80 flasktest 
```

### docker build
To build image use `Dockerfile` content and run
```shell
docker build -t gagarin .
```

### manual deploy
For deploy app manually 
```shell
kubectl create deployment gagarin --image=gagarin:latest
kubectl expose deployment gagarin --type=NodePort --port=5000
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
kubectl port-forward service/gagarin 8080:5000
```

### script deploy

### redeploy

## Links
* kubernetes docs https://kubernetes.io/ru/docs/home/
* Azure Cloud https://portal.azure.com/?quickstart=true#blade/Microsoft_Azure_Resources/QuickstartCenterBlade  27.11.2021

## Next TO DO
* deploy to another cluster
