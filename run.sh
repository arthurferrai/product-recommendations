#!/usr/bin/env bash
echo Setting environment
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
echo Using host ${1:-'127.0.0.1'} on port ${2:-3000}
python src/main.py ${1:-'127.0.0.1'} ${2:-3000}
deactivate
