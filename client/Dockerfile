FROM node:lts-alpine
MAINTAINER Raul Cioldin <raulvc@gmail.com>

RUN npm install -g http-server
WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080