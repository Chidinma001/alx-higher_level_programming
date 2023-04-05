#!/bin/bash
# Display allowed HTTP methods
curl -sI "$1" | grep "Allow:" | sed 's/Allow: //g'
