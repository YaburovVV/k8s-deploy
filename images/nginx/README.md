# nginx
Nginx was set for browsing files

@journey

Build app
```shell
docker run -v ./../../:/usr/share/nginx/html:ro -v ./nginx.conf:/etc/nginx/conf.d/default.conf:ro -p 80:80 -d nginx
```
$ docker run -p 8080:80 -v /path/to/my/files/:/opt/www/files/ mohamnag/nginx-file-browser