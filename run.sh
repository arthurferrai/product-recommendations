#!/usr/bin/env bash
echo Using host ${1:-'127.0.0.1'} on port ${2:-3000}
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py ${1:-'127.0.0.1'} ${2:-3000}
deactivate
