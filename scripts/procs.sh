#!/bin/bash

openUrl() {
	if [ $# -ne 1 ]; then
		echo "Expected a single URL parameter"
		exit 1
	fi

	URL=$1

	case "$OSTYPE" in
		darwin*)  open $URL ;;
		linux*)   xdg-open $URL ;;
		*)        echo "unknown OS: $OSTYPE.  Open URL $URL manually" ;;
	esac
}

runCosmicRay() {
	cosmic-ray init cosmic-ray.unittest.yaml cosmic-ray-session
	cosmic-ray exec cosmic-ray-session
	if [ ! -d $CR_DIR ]; then
		mkdir -p $CR_DIR
	fi	
	CR_FILE=$CR_DIR/index.html
	cosmic-ray dump cosmic-ray-session | cr-html > $CR_FILE
	openUrl $CR_FILE	
}
