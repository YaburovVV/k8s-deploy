# flask app
Sample python app contains 2 files 
* api-server.py
* requirements.txt

@journey

#### Run the service docker locally

```shell
docker ps -a
```
```shell
docker images
```
Clear containers
```shell
docker ps -a
docker rm $(docker ps -aq)
```
Get images versions
```shell
curl -s https://hub.docker.com/v2/repositories/yaburov/flask-app/tags | jq '{versions: [.results[] | .name ]}'
```

Build app
```shell
docker build -t yaburov/flask-app:3 .
docker images
```
Push app to hub.docker.com
```shell
docker push yaburov/flask-app:3
```

Run app
```shell
docker run -it -p 80:80 yaburov/flask-app:3 
```

#### build it for GCP
```shell
docker buildx build -t yaburov/flask-app-gcp:1 --platform linux/x86_64 .  
docker push yaburov/flask-app-gcp:1
```

Run app
```shell
docker run -it -p 80:80 yaburov/flask-app-gcp:1 
```

#### Run the service locally
```shell
python3 -m venv venv
source venv/bin/activate  
pip install -r requirements.txt   
export FLASK_APP=api-server  
python -m flask run --host=0.0.0.0 --port=80
```
Remove venv
```shell
deactivate
rm -fr venv
```