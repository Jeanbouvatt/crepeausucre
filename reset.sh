source ./openrc.sh
rm OUR_KEY.pem
openstack keypair delete PRIMARY_KEY
openstack server delete server-w server-i server-s server-p server-b server-frontend

