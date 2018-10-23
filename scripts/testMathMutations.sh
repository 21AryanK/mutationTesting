#!/bin/bash

ORIG_CWD=$PWD
SCRIPT_DIR=$(dirname $0)
source $SCRIPT_DIR/procs.sh

cd $SCRIPT_DIR/..
runMutationTests AOR
cd $ORIG_CWD
