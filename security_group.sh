GROUP_NAME=$1

openstack security group create $GROUP_NAME --description "Groupe de sécurité pour les VM"

openstack security group rule create $GROUP_NAME --proto tcp --dst-port 80:80 --src-ip 0.0.0.0/0
openstack security group rule create $GROUP_NAME --proto tcp --dst-port 8090:8090 --src-ip 0.0.0.0/0
openstack security group rule create $GROUP_NAME --proto tcp --dst-port 8091:8091 --src-ip 0.0.0.0/0
openstack security group rule create $GROUP_NAME --proto tcp --dst-port 8092:8092 --src-ip 0.0.0.0/0
openstack security group rule create $GROUP_NAME --proto tcp --dst-port 8093:8093 --src-ip 0.0.0.0/0
openstack security group rule create $GROUP_NAME --proto tcp --dst-port 8095:8095 --src-ip 0.0.0.0/0

