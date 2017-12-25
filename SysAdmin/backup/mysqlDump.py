#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Python script to backup a MySql database
# Tested using Python 2.6.6 on a MySql 5.1 database
# 
# Michael Wakahe, michael@michaelwakahe.com
#
# Remember to set the correct root password for your MySQL installation.
#
# Restore the compressed dump files as follows.
# As MySQL root user, create the database:
#      mysql> create database databaseName;
# 
# Then import the dumped file from the shell:
#      $ gunzip -c dumpfile.gz | mysql -u root -p[root_password] databaseName
#
# You then have to change ownership of the database to the original user.
# As MySQL root user:
#      mysql> GRANT ALL PRIVILEGES ON databaseName.* TO 'databaseUser'@'localhost' IDENTIFIED BY 'dbPassword';
#      mysql> GRANT ALL PRIVILEGES ON databaseName.* TO 'databaseUser'@'%' IDENTIFIED BY 'dbPassword';
#      mysql> FLUSH PRIVILEGES;
#
# After restoration, it's a good idea to remove the root MySQL password from 
# the history, This can be done with the following commands:
#     $ rm -rf ~/.bash_history; history -c
# -------------------------------------------------------------------------

import ConfigParser
import os
import time

# On Debian, /etc/mysql/debian.cnf contains 'root' a like login and password.
#config = ConfigParser.ConfigParser()
#config.read("/etc/mysql/debian.cnf")
#username = config.get('client', 'user')
#password = config.get('client', 'password')
#hostname = config.get('client', 'host')
username = "root"
password = "root"
hostname = "localhost"

filestamp = time.strftime('%d-%m-%Y')

# Get a list of databases with:
database_list_command="mysql -u %s -p%s -h %s --silent -N -e 'show databases'" % (username, password, hostname)
for database in os.popen(database_list_command).readlines():
    database = database.strip()
    if database == 'information_schema':
        continue
    filename = "/mnt/Backup/dumps/mysql/%s-%s.sql" % (database, filestamp)
    os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (username, password, hostname, database, filename))
