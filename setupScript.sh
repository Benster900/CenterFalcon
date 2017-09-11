#!/bin/bash

# Add user
useradd centerfalcon

# Copy service
cp contrib/systemd/centerfalcon.service /etc/systemd/system/

# Install things
yum install python-pip -y
pip install virtualenv

cd /opt/centerfalcon
source env/bin/active
pip install -r requirements.txt

# Start service
systemctl enable centerfalcon.service
systemctl start centerfalcon.service
