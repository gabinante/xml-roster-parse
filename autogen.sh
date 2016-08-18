#!/bin/bash

curl http://alteraeon.com:8080/xml/clan/15 > /var/www/html/roster.xml
cd /var/www/html
python xmlparse.py
(sed -n '1,/^<!-- BEGIN realm -->/p' index.html; cat autoroster.html; sed -n '/^<!-- END realm -->/,$p' index.html) > index2.html
mv index2.html index.html
