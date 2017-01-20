#!/bin/bash
source ./openrc.sh
echo $1
FLAVOR="m1.small"
NIC="net-id=a992853b-b9cf-42c7-9b7e-e3e8fecd58fb"
IMAGE=ubuntu1604
KEY_NAME="KEY_NAME"
SECURITY="default"
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

