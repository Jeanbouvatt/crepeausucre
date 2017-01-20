#!/bin/bash
#argument: $1 : name of server
# $2 : security group
# $3 : directory to upload
# $4 : KEY
# $5 : remote script to execute

FLAVOR="m1.small"
NIC="net-id=a992853b-b9cf-42c7-9b7e-e3e8fecd58fb"
IMAGE=ubuntu1604
KEY=$4
SECURITY=$2
NAME=$1
DIR=$3
SCRIPT=$5
ID="[service $1 creator]"
echo "$ID create service with : name : $1
security group : $2
directory to upload : $3
key : $4
remote script : $5"
IP=$(openstack server list | grep $NAME | cut -d = -f 2 | cut -d '|' -f 1)
if [ "$IP" == "" ]
then
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY $NAME --key-name $KEY
while [ "$IP" != "" ]
do
	echo "$ID waiting for end of server building"
	sleep 3
	IP=$(openstack server list | grep $NAME | cut -d = -f 2 | cut -d '|' -f 1)
done
fi
echo "$ID : server succesfully created with ip : $IP" 
echo "$DIR $IP"
scp -i $KEY -r $DIR "ubuntu@$IP:~"
echo "$ID copy finished"
ssh -i $KEY ubuntu@"$IP" "$SCRIPT"
echo "$ID ssh script succesfull" 
