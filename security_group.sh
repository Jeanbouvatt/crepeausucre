group_name=VM_Group


openstack security group create $group_name --description "Groupe de sécurité pour les VM"

openstack security group rule create VM_Group --protocol tcp --dst-port 80:80 --remote-ip 0.0.0.0/0
openstack security group rule create VM_Group --protocol tcp --dst-port 8090:8090 --remote-ip 0.0.0.0/0
openstack security group rule create VM_Group --protocol tcp --dst-port 8091:8091 --remote-ip 0.0.0.0/0
openstack security group rule create VM_Group --protocol tcp --dst-port 8092:8092 --remote-ip 0.0.0.0/0
openstack security group rule create VM_Group --protocol tcp --dst-port 8093:8093 --remote-ip 0.0.0.0/0
openstack security group rule create VM_Group --protocol tcp --dst-port 8095:8095 --remote-ip 0.0.0.0/0

