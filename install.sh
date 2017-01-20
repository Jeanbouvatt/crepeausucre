#!/bin/bash
source ./openrc.sh
echo $1
FLAVOR="m1.small"
NIC="net-id=a992853b-b9cf-42c7-9b7e-e3e8fecd58fb"
IMAGE=ubuntu1604
KEY_NAME="KEY_NAME"
SECURITY="default"
#<<<<<<< HEAD

if [ $(ls MY_KEY.pem | wc -l) != 1 ]
	then
	openstack keypair create KEY_NAME > MY_KEY.pem
	chmod 600 MY_KEY.pem
	fi
#TODO : security things
#creating i s b w p frontend
if [ $1 ] 
	then
	openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_i --key-name $KEY_NAME
	openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_s --key-name $KEY_NAME
	openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_b --key-name $KEY_NAME
	openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_w --key-name $KEY_NAME
	openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY sub_p --key-name $KEY_NAME
	openstack server create --flavor $FLAVOR --image $IMAGE --nic $NIC --security-group $SECURITY frontend --key-name $KEY_NAME

sleep 2m 
fi

DIR="cloud_native_app/microservices"
#TODO retrieve IP address from i s b w p frontend
sleep 10
IP_I=$(openstack server list | grep sub_i | cut -d = -f 2 | cut -d '|' -f 1)
echo $IP_I
IP_S=$(openstack server list | grep sub_s | cut -d = -f 2 | cut -d '|' -f 1)
echo $IP_S
IP_B=$(openstack server list | grep sub_b | cut -d = -f 2 | cut -d '|' -f 1)
IP_W=$(openstack server list | grep sub_w | cut -d = -f 2 | cut -d '|' -f 1)
IP_P=$(openstack server list | grep sub_p | cut -d = -f 2 | cut -d '|' -f 1)
IP_FRONTEND=$(openstack server list | grep frontend | cut -d = -f 2 | cut -d '|' -f 1)

scp -i MY_KEY.pem -r $DIR/i $IMAGE@$IP_I
scp -i MY_KEY.pem -r $DIR/s $IMAGE@$IP_S
scp -i MY_KEY.pem -r $DIR/b $IMAGE@$IP_B
scp -i MY_KEY.pem -r $DIR/w $IMAGE@$IP_W
scp -i MY_KEY.pem -r $DIR/p $IMAGE@$IP_P
scp -i MY_KEY.pem -r 'cloud_native_app/frontend' $IMAGE@$IP_FRONTEND
#=======
if [ "$1" == "gen_key" ]; then
	openstack keypair create KEY_NAME > MY_KEY.pem
	chmod 600 MY_KEY.pem
fi
#TODO : security things
#creating i s b w p frontend
if [ "$1" == "test" ]; then
	  echo "testing script"
fi
DIR="cloud_native_app/microservices"
./setup_service.sh "server_i" "default" $($DIR/i) $KEY_NAME $($DIR/i/install.sh) 
#./setup_service.sh "server_s" "default" $($DIR/s) $KEY_NAME $($DIR/s/install.sh) 
#./setup_service.sh "server_b" "default" $($DIR/b) $KEY_NAME $($DIR/b/install.sh) 
#./setup_service.sh "server_w" "default" $($DIR/w) $KEY_NAME $($DIR/w/install.sh) 
#./setup_service.sh "server_p" "default" $($DIR/p) $KEY_NAME $($DIR/p/install.sh) 
#./setup_service.sh "server_frontend" "default" $(cloud_native_app/frontend) $KEY_NAME $(cloud_native_app/frontend/install.sh) 
echo "done"
#>>>>>>> 2b22b9ad605d11f19fab8f3432efa1c58c1c7ebc

