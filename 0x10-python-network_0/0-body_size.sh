#!/bin/bash
#Takes in URL, sends request to URL, displays size of body of response
curl -w '%{size_download}\n' -so /dev/null "$1"
