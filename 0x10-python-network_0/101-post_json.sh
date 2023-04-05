#!/bin/bash
# POST request to a URL passed as first argument
curl -s -H "Content-Type: application/json" -X POST -d "@$2" "$1"
