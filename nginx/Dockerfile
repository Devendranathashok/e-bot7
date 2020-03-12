FROM nginx:latest
MAINTAINER Devendranath Ashok

RUN apt-get update
RUN apt-get install apache2-utils -y
RUN echo e-bot7 | htpasswd -ic /etc/nginx/.htpasswd admin
COPY default.conf /etc/nginx/conf.d/
COPY index.html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
