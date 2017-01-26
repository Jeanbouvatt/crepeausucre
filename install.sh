#!/bin/bash
source ./openrc.sh
echo $1
RED='\033[0;31m'
NC='\033[0m'
ID="{$RED}[main installer]{$NC}"
FLAVOR="m1.small"
IMAGE=ubuntu1604
KEY_FILE="OUR_KEY.pem"
KEY_NAME="PRIMARY_KEY"
SECURITY="default"
#SUB_SECU="sub_security_group_8"
SUB_SECU="default"
DIR="cloud_native_app/microservices"
NETWORK_NAME="private8"
#setting up security
CONF_FILE="conf"
rm $CONF_FILE 2>/dev/null
if [ "$1" == "reset-security" ]
then
	echo "$ID creating security group"
	./security_group.sh $SUB_SECU
fi

#setting up key for ssh access
if [ ! -f $KEY_FILE ]
then
	echo "$ID creating new key"
	openstack keypair create $KEY_NAME > $KEY_FILE
	chmod 600 $KEY_FILE
fi

#creating i s b w p frontend

#yes | ./setup_service.sh "i" $SUB_SECU "$DIR/i" $KEY_NAME $KEY_FILE "i/install.sh" $NETWORK_NAME $CONF_FILE &
#yes | ./setup_service.sh "s" $SUB_SECU "$DIR/s" $KEY_NAME $KEY_FILE "s/install.sh" $NETWORK_NAME $CONF_FILE &
#yes | ./setup_service.sh "b" $SUB_SECU "$DIR/b" $KEY_NAME $KEY_FILE "b/install.sh" $NETWORK_NAME $CONF_FILE &
yes | ./setup_service.sh "w" $SUB_SECU "$DIR/w" $KEY_NAME $KEY_FILE "w/install.sh" $NETWORK_NAME $CONF_FILE &
#yes | ./setup_service.sh "p" $SUB_SECU "$DIR/p" $KEY_NAME $KEY_FILE "p/install.sh" $NETWORK_NAME $CONF_FILE & 
#yes | ./setup_service.sh "frontend" default "cloud_native_app/frontend" $KEY_NAME $KEY_FILE "frontend/install.sh" $NETWORK_NAME $CONF_FILE

echo "$ID finished"
