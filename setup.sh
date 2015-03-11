#!/bin/bash
apt-get -y install supervisor
cp -v shutdown.conf /etc/supervisor/conf.d/
cp -v shutdown.py /usr/local/bin/
mkdir -p /var/log/shutdown
service supervisor restart
