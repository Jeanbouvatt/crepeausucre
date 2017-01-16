FROM debian:jessie
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN apt-get install -y python3-flask
RUN apt-get install -y mysql-server 
RUN apt-get install -y libmysqlclient-dev 
RUN apt-get install -y python-dev 
RUN apt-get install -y python-mysqldb 
RUN apt-get install -y python3-mysql.connector
RUN mysql_secure_installation
RUN pip install mysql
RUN pip install MYSQL-python
RUN pip install mysql-connector-python --allow-external mysql-connector-python
RUN apt-get install -y imagemagick
RUN useradd i
COPY config.py i.conf i.py /home/i/
RUN chown -R i:i /home/i/
EXPOSE 8090
USER i
WORKDIR /home/i
