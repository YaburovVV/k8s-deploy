# Install Ingress Controller: Contour
```shell
kubectl apply -f https://projectcontour.io/quickstart/contour.yaml
kubectl get services -n projectcontour envoy -o wide
```

Get LoadBalancer IP or DNS Name and assign Your Domain to this DNS name

### Create Deployments
```shell
kubectl create deployment main   --image=adv4000/k8sphp:latest
kubectl create deployment web1   --image=adv4000/k8sphp:version1
kubectl create deployment web2   --image=adv4000/k8sphp:version2
kubectl create deployment webx   --image=adv4000/k8sphp:versionx
kubectl create deployment tomcat --image=tomcat:8.5.38
```
### Scale Deployments
```shell
kubectl scale deployment main  --replicas 2
kubectl scale deployment web1  --replicas 2
kubectl scale deployment web2  --replicas 2
kubectl scale deployment webx  --replicas 2
```
### Create Services, default type is: --type=ClusterIP
```shell
kubectl expose deployment main   --port 80
kubectl expose deployment web1   --port 80
kubectl expose deployment web2   --port 80
kubectl expose deployment webx   --port 80
kubectl expose deployment tomcat --port 8080
```
```shell
kubectl get services -o wide
```
```shell
kubectl apply -f ingress-hosts.yaml
kubectl apply -f ingress-paths.yaml
kubectl get ingress
kubectl describe ingress
```
### Completely delete Ingress Controller: Contour
```shell
kubectl delete ns projectcontour
```