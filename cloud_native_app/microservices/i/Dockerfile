FROM debian:jessie
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
apt-get install -y python3 python3-flask python3-requests
RUN apt-get install -y imagemagick
RUN useradd i
COPY config.py i.conf i.py /home/i/
RUN chown -R i:i /home/i/
EXPOSE 8091
USER i
WORKDIR /home/i
