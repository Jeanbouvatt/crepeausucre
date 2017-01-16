FROM debian:jessie
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
apt-get install -y python3 python3-flask
RUN apt-get install -y imagemagick
RUN useradd b
COPY config.py b.conf b.py /home/b/
RUN chown -R b:b /home/b/
EXPOSE 8093
USER b
WORKDIR /home/b
