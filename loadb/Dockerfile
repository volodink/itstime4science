FROM nginx
MAINTAINER Konstantin Volodin, volodin.konstantin@gmail.com

COPY nginx.conf /etc/nginx

EXPOSE 80
EXPOSE 5500

ENTRYPOINT nginx -g "daemon off;"
