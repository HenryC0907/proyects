#!/bin/bash

open_ports=$(netstat -tln | awk '{print $4}' |tr -d "local" | tr -d "(dy" | sed 's/:/ /g' | awk '{print $2}')

echo "Puertos abiertos: $open_ports"
