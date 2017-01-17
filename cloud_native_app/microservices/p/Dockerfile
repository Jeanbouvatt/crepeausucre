FROM debian:jessie
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
apt-get install -y python3 python3-flask
RUN apt-get install -y imagemagick
RUN useradd p
COPY config.py p.conf p.py /home/p/
COPY prices /home/p/prices/
RUN chown -R p:p /home/p/
EXPOSE 8094
USER p
WORKDIR /home/p
CMD ["./p.py"]
