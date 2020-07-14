#!/bin/bash

echo 'creating virtual environment'
python3 -m venv venv
source venv/bin/activate

echo 'python libraries installation'
pip3 install -r requirements.txt
