#!/bin/bash

SCRIPT_DIR=$(dirname $0)
source $SCRIPT_DIR/procs.sh

pytest --cov-report=html --cov=simplenumber tests/
openUrl htmlcov/index.html
