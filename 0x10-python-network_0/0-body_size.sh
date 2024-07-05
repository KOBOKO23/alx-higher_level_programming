#!/bin/bash
# displays body size of HTTP response in bytes
curl -sI "$1" | wc -c
