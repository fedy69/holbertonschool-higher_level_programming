#!/bin/bash
#Takes in URL, sends GET request and displays body of response 
curl -s -X GET "$1" -H "X-School-User-Id:98"
