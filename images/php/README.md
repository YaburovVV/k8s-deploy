# php app
Sample php app for try it in k8s

@journey

#### Run the service docker locally

Get images versions
```shell
curl -s https://hub.docker.com/v2/repositories/yaburov/httpd-php/tags | jq '{versions: [.results[] | .name ]}'
```

Build app
```shell
docker build -t yaburov/httpd-php:2 .
docker images
```
Push app to hub.docker.com
```shell
docker push yaburov/httpd-php:2
```

Run app
```shell
docker run -it -h httpd-php.com -p 80:80 yaburov/httpd-php:2 
```
