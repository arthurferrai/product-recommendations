#!/usr/bin/env bash
echo Setting environment
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
echo Testing flask endpoints
python -m unittest src.tests.FlaskServerTest
deactivate
