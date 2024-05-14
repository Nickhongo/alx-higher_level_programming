#!/bin/bash

# This script takes a URL as an argument, sends a request to that URL,
# and displays the size of the response body in bytes
curl -s "$1" | wc -c
