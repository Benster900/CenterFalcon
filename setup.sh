#!/bin/bash
# Create directory to drop malware
mkdir /opt/yara_malware

# Add user
useradd centerfalcon

# Install pip
yum install pip -y

# Install virtualenv
virtualenv env

# Setup env
source env/bin/activate
pip install -r requirements.txt
