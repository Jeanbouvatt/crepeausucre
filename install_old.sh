#!/bin/sh
source ./openrc.sh
echo $1
FLAVOR="m1.tiny"
NIC="net-id=a992853b-b9cf-42c7-9b7e-e3e8fecd58fb"
IMAGE=ubuntu1604
KEY_NAME="KEY_NAME"
SECURITY="default"

openstack keypair create KEY_NAME > MY_KEY.pem
chmod 600 MY_KEY.pem
#TODO : security things
#creating i s b w p frontend
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_i --key-name $KEY_NAME
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_s --key-name $KEY_NAME
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_b --key-name $KEY_NAME
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_w --key-name $KEY_NAME
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_p --key-name $KEY_NAME
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY frontend --key-name $KEY_NAME
DIR="cloud_native_app/microservices"
#TODO retrieve IP address from i s b w p frontend
scp -i MY_KEY.pem -r $DIR/i $IMAGE@$IP_I
scp -i MY_KEY.pem -r $DIR/s $IMAGE@$IP_S
scp -i MY_KEY.pem -r $DIR/b $IMAGE@$IP_B
scp -i MY_KEY.pem -r $DIR/w $IMAGE@$IP_W
scp -i MY_KEY.pem -r $DIR/p $IMAGE@$IP_P
scp -i MY_KEY.pem -r #TODO frontend $IMAGE@$IP_FRONTEND

ssh -i MY_KEY.pem $IMAGE@$IP_I 'bash -s' < $DIR/i/install.sh
ssh -i MY_KEY.pem $IMAGE@$IP_S 'bash -s' < $DIR/s/install.sh
ssh -i MY_KEY.pem $IMAGE@$IP_B 'bash -s' < $DIR/b/install.sh
ssh -i MY_KEY.pem $IMAGE@$IP_W 'bash -s' < $DIR/w/install.sh
ssh -i MY_KEY.pem $IMAGE@$IP_P 'bash -s' < $DIR/p/install.sh
ssh -i MY_KEY.pem $IMAGE@$IP_FRONTEND 'bash -s' < #TODO$DIR/install.sh
