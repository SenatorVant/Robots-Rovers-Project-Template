#!/bin/bash

sudo apt update
sudo apt install python3-pip php libatlas-base-dev -y

pip3 install -r requirements.txt

echo "Setup complete"
