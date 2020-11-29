#!/bin/sh
# Script to get number of clients connected

echo $( cat /tmp/dhcp.leases|wc -l )
