#!/usr/bin/env bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
export SERVER_NAME=127.0.0.1:3000
python src/main.py
