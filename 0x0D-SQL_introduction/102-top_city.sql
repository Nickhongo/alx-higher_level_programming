#!/bin/bash

MYSQL_USER="your_mysql_username"
MYSQL_PASSWORD="your_mysql_password"
DATABASE="hbtn_0c_0"

mysql -u $MYSQL_USER -p$MYSQL_PASSWORD $DATABASE < table_dump.sql

mysql -u $MYSQL_USER -p$MYSQL_PASSWORD $DATABASE -e "SELECT city, temperature FROM temperatures WHERE month IN ('July', 'August') ORDER BY temperature DESC LIMIT 3;"

