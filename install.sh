#!/bin/sh

echo $1
FLAVOR="m1.tiny"
NIC="net-id=a992853b-b9cf-42c7-9b7e-e3e8fecd58fb"
IMAGE=ubuntu1604
KEY_NAME="KEY_NAME"
SECURITY="default"

openstack keypair create KEY_NAME > MY_KEY.pem
chmod 600 MY_KEY.pem
#creating i s b w p frontend
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_i --key-name $KEY_NAME
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_s --key-name $KEY_NAME
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_b --key-name $KEY_NAME
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_w --key-name $KEY_NAME
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_p --key-name $KEY_NAME
openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY frontend --key-name $KEY_NAME

#TODO retrieve IP address from i s b w p frontend
scp -i MY_KEY.pem -r i $IMAGE@$IP_I
scp -i MY_KEY.pem -r s $IMAGE@$IP_S
scp -i MY_KEY.pem -r b $IMAGE@$IP_B
scp -i MY_KEY.pem -r w $IMAGE@$IP_W
scp -i MY_KEY.pem -r p $IMAGE@$IP_P
scp -i MY_KEY.pem -r frontend IMAGE@$IP_FRONTEND

ssh -i MY_KEY.pem $IMAGE@$IP_I 'bash -s' < install_i.sh
ssh -i MY_KEY.pem $IMAGE@$IP_S 'bash -s' < install_s.sh
ssh -i MY_KEY.pem $IMAGE@$IP_B 'bash -s' < install_b.sh
ssh -i MY_KEY.pem $IMAGE@$IP_W 'bash -s' < install_w.sh
ssh -i MY_KEY.pem $IMAGE@$IP_P 'bash -s' < install_p.sh
ssh -i MY_KEY.pem $IMAGE@$IP_FRONTEND 'bash -s' < install_frontend.sh
