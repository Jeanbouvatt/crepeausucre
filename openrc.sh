#!/bin/sh

# To use an OpenStack cloud you need to authenticate against the Identity
# service named keystone, which returns a **Token** and **Service Catalog**.
# The catalog contains the endpoints for all services the user/tenant has
# access to - such as Compute, Image Service, Identity, Object Storage, Block
# Storage, and Networking (code-named nova, glance, keystone, swift,
# cinder, and neutron).
#
# *NOTE*: Using the 2.0 *Identity API* does not necessarily mean any other
# OpenStack API is version 2.0. For example, your cloud provider may implement
# Image API v1.1, Block Storage API v2, and Compute API v2.0. OS_AUTH_URL is
# only for the Identity API served through keystone.
#export OS_AUTH_URL=http://10.11.50.26:5000/v3
export OS_AUTH_URL=http://10.11.50.26:5000/v2.0
echo $OS_AUTH_URL

# With the addition of Keystone we have standardized on the term **tenant**
# as the entity that owns the resources.
export OS_TENANT_ID=8416eb6bb2294f688f62641e8d3a3a45
export OS_TENANT_NAME="project8"

# unsetting v3 items in case set
unset OS_PROJECT_ID
unset OS_PROJECT_NAME
unset OS_USER_DOMAIN_NAME

# In addition to the owning entity (tenant), OpenStack stores the entity
# performing the action as the **user**.
export OS_USERNAME="groupe8"

# With Keystone you pass the keystone password.
export OS_PASSWORD="UkkXisg5zDo="

# If your configuration has multiple regions, we set that information here.
# OS_REGION_NAME is optional and only valid in certain environments.
export OS_REGION_NAME="region1"
# Don't leave a blank variable, unset it if it was empty
if [ -z "$OS_REGION_NAME" ]; then unset OS_REGION_NAME; fi
