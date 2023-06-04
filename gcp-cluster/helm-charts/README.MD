# Helm commands

```shell
helm list
helm search repo
helm search hub
```

```shell
helm install app1 dir1
helm upgrade app1 dir1  --set container.image=myimage:v1
```

```shell
helm create chart1
helm package chart1 
helm install MyChart-0.1.tgz
helm delete app1 
helm uninstall app1 
```

```shell
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install app1 bitnami/apache -f values.yml
```