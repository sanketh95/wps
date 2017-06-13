#!/bin/bash

while true ; do
    nmcli -t -f SSID,SIGNAL dev wifi | tr '\n' ';' | awk '{sub(/;$/,"");print}' >> $1
    sleep 0.5
done
