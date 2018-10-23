#!/bin/bash

ORIG_CWD=$PWD
SCRIPT_DIR=$(dirname $0)
source $SCRIPT_DIR/procs.sh

cd $SCRIPT_DIR/..
runMutationTests ROR
openUrl .mutpy/index.html
cd $ORIG_CWD
