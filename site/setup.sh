#!/bin/bash

echo 'creating virtual environment'
python3 -m venv venv || { echo 'creating virtual environment failed' ; exit 1; }
source venv/bin/activate || { echo 'activating virtual environment failed' ; exit 1; }

echo 'python libraries installation'
pip3 install -r requirements.txt
