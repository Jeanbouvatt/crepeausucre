FROM debian:jessie
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y php5 apache2 php5-curl
COPY www/ /var/www/html
RUN rm /var/www/html/index.html
EXPOSE 80
CMD /etc/init.d/apache2 start

