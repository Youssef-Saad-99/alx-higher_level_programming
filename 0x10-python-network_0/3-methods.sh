#!/bin/bash
# This script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f2-
