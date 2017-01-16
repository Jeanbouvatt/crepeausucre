FROM debian:jessie
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
apt-get install -y python3 python3-flask
RUN apt-get install -y imagemagick
RUN useradd frontend
COPY config.py frontend.conf frontend.py /home/frontend/
COPY prices /home/w/prices/
RUN chown -R frontend:frontend /home/frontend/
EXPOSE 8090
USER frontend
WORKDIR /home/frontend
CMD ["./frontend.py"]
