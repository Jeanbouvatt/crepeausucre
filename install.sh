#!/bin/bash
source ./openrc.sh
echo $1
FLAVOR="m1.small"
NIC="net-id=a992853b-b9cf-42c7-9b7e-e3e8fecd58fb"
IMAGE=ubuntu1604
KEY="MY_KEY.pem"
SECURITY="default"
DIR="cloud_native_app/microservices"

if [ $(ls MY_KEY.pem | wc -l) != 1 ]
then
openstack keypair create KEY_NAME > $KEY
chmod 600 MY_KEY.pem
fi
#TODO : security things
./setup_security.sh "sub-services"
#creating i s b w p frontend
echo  "calling setup service on shits and things"
./setup_service.sh "server_i" "default" "$DIR/i" $KEY "i/install.sh" &
./setup_service.sh "server_s" "default" $($DIR/s) $KEY_NAME $($DIR/s/install.sh) & 
./setup_service.sh "server_b" "default" $($DIR/b) $KEY_NAME $($DIR/b/install.sh) &
./setup_service.sh "server_w" "default" $($DIR/w) $KEY_NAME $($DIR/w/install.sh) &
./setup_service.sh "server_p" "default" $($DIR/p) $KEY_NAME $($DIR/p/install.sh) &
#TODO : correct front end so it can access sub-service
./setup_service.sh "server_frontend" "default" $(cloud_native_app/frontend) $KEY_NAME $(cloud_native_app/frontend/install.sh) 
#TODO : setup floating ip for front end"
