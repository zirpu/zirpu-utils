#!/bin/bash

host="$1"
if [ -z "$host" ]; then
  echo "usage: $0 FQDN"
  exit 1
fi

# generate self-signed webserver keys.

openssl genrsa -out $host.key 2048
openssl req -new -key $host.key -out $host.csr
openssl x509 -req -days 1000 -in $host.csr -signkey $host.key -out $host.crt


