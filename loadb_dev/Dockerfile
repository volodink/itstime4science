FROM nginx:alpine
MAINTAINER Konstantin Volodin, volodin.konstantin@gmail.com

COPY nginx.conf /etc/nginx

EXPOSE 80

ENTRYPOINT nginx -g "daemon off;"
