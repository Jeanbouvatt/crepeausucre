FROM debian:jessie
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
apt-get install -y python3 python3-flask python3-requests
RUN apt-get install -y imagemagick
RUN useradd s
COPY config.py s.conf s.py /home/s/
RUN chown -R s:s /home/s/
EXPOSE 8092
USER s
WORKDIR /home/s
CMD ["./s.py"]
