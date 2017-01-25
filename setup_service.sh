#!/bin/bash
#argument: $1 : name of server
# $2 : security group
# $3 : directory to upload
# $4 : KEY_NAME
# $5 : KEY_FILE
# $6 : remote script to execute
# $7 : Network
FLAVOR="m1.small"
IMAGE=ubuntu1604

NAME="server-$1"
SECURITY=$2
DIR=$3
KEY_NAME=$4
KEY_FILE=$5
SCRIPT=$6
NETWORK_NAME=$7
CONF_FILE=$8
RED='\033[0;31m'
NC='\033[0m'
ID="$RED[service $1 creator]$NC"
echo -e "$ID create service with : name : $1
security group : $2
directory to upload : $3
key name : $4
key file : $5
remote script : $6
network : $7
configuration file for frontend : $8"

#retrieving network id
NIC=$(openstack network list | grep $NETWORK_NAME | cut -d '|' -f 2 | cut -d ' ' -f 2)
NIC="net-id=$NIC" 
#retrieving server IP
IP=$(openstack server list | grep $NAME | cut -d = -f 2 | cut -d '|' -f 1 | cut -d ',' -f 1 | cut -d ' ' -f 1)
if [ "$IP" == "" ]
then
	openstack server create --flavor $FLAVOR --image $IMAGE --security-group $SECURITY $NAME --key-name $KEY_NAME --nic $NIC
	echo -e "$ID server created, ongoing build"
	while [ "$IP" == "" ]
	do	
		echo -e "$ID waiting for end of server building"
		sleep 3
		IP=$(openstack server list | grep $NAME | cut -d = -f 2 | cut -d '|' -f 1 | cut -d ',' -f 1 | cut -d ' ' -f 1)
	done
	echo -e "$ID : server succesfully created with ip : $IP" 
	echo -e "$ID now sleeping 1 minute  to let ssh access be accepted"
	sleep 1m
fi
if [ "$1" != "frontend" ]
then 
	echo -e "$1=$IP:$(./port.sh $1)" >> $CONF_FILE
fi 
#now copying installation files
scp -o "StrictHostKeyChecking=no" -i $KEY_FILE -r $DIR "ubuntu@$IP:~"
echo -e "$ID copy finished"
#running install script
ssh -o "StrictHostKeyChecking=no" -i $KEY_FILE ubuntu@"$IP" "$SCRIPT"
echo -e "$ID ssh script finished" 

#updating conf file if frontend.
if [ "$1" == "frontend" ]
then
	while [ $(wc -l $CONF_FILE | cut -d ' ' -f 1) -lt 5 ]
	do
		echo -e "$ID Waiting for all IP to be provided"
		sleep 10
	done
	scp -i $KEY_FILE $CONF_FILE "ubuntu@$IP:~/frontend/www/conf"
	echo -e "$ID Done"
fi
