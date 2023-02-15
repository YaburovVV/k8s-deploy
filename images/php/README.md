# php app
Sample php app for try it in k8s

#### for trying locally
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
docker build -t php-app .
docker run -it -p 80:80 flasktest 
```
#### build it for GCP
```shell
docker buildx build -t yaburov/flask-app:1 --platform linux/x86_64 .  
docker push yaburov/flask-app:1
```

