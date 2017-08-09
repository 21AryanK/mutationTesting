#!/bin/bash

SCRIPT_DIR=$(dirname $0)
source $SCRIPT_DIR/procs.sh

coverage run --branch --source=simplenumber -m unittest discover -s tests/
coverage html
openUrl htmlcov/index.html
