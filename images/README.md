# samples images

#### for trying docker locally
```shell
docker build -t app .
docker run -it -p 80:80 flasktest
```
#### build it for GCP
```shell
docker buildx build -t yaburov/app --platform linux/x86_64 .  
docker push yaburov/app
```

