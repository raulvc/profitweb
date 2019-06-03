# profitweb
A simple test project exposing features of some recent and fairly known frameworks (as of 2019)

![alt text](https://github.com/raulvc/profitweb/blob/master/docs/img/showcase.png)

# Live demo
http://ec2-18-219-192-131.us-east-2.compute.amazonaws.com:8080/

# Instructions
- Get [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/)
- With your cwd placed at the project's root:
```
$ docker-compose up
```

# Development
## Backend
Server is written in python with [django's rest framework](https://www.django-rest-framework.org/) using almost no third party projects;
Database is set to SQLite;
Dependencies can be seen in [requirements.txt](https://github.com/raulvc/profitweb/blob/master/server/requirements.txt).

## Frontend
Webclient written in js with [Vue](https://vuejs.org/) and ui components from [Vuetify](https://vuetifyjs.com);
Webpack's version is set to 3 (thus the alerts from github)
