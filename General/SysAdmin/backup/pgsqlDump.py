#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Python script to backup a PostgreSQL database
# Tested using Python 2.6.6 on a PostgreSQL 8.4.7 database
#
# Michael Wakahe, michael@michaelwakahe.com
#
# Ensure the file .pgpass in a user's home directory for passwordless command 
# line authentication. 
# 
# The format of the .pgpass file is the following:
#     hostname:port:database:username:password 
# The character '*' can match any value in any of the fields (except password)
# So for example, for a user to be able to access all databases locally:
#     localhost:5432:*:postgres:rootPostgresPassword
# Lines in the .pgpass file beginning with a '#' are ignored.
# n.b.: if the environment variable PGPASSWORD is set, then the ~/.pgpass file
# is not read
#
# You have to set its permissions to 0600 i.e. "chmod 0600 ~/.pgpass"
#
# 
# To restore a dump, you should also re-create the role that previously 
# owned the database before doing an import.   
#  
# To create the role, for production environments:
# First become user "postgres" at the shell.
# Then execute the following to create a new user:
#    $ createuser --createdb --pwprompt --encrypted YOUR_USERNAME
#
# If you have to execute SQL scripts which involve reading/writing of data to 
# an external file, you must use the superuser 'postgres' to do so. In 
# production environments, new database users should never be superusers 
# otherwise they can read/alter tables that they did not create.
#
# Once you have created the role, log into the database shell with that 
# username and create the database as follows:
#    $ psql -h localhost -U YOUR_USERNAME postgres
#    postgres=> CREATE DATABASE dbname;
#  
# Restore the compressed dump files as follows:
#    $ gunzip -c dumpfile.gz | psql [--host hostname] [--port port] [-U username] [-W] dbname
#
# You may get an error when restoring as follows. You will then be prompted to
# enter your database password again. 
#    ERROR:  database "dbname" already exists
# Just do as prompted and ignore it.
#
# -----------------------------------------------------------------------------

import os
import time

username = "postgres"
hostname = "localhost"

filestamp = time.strftime('%d-%m-%Y')

# Get a list of databases with:
database_list_command="psql -U %s -h %s -c 'SELECT datname FROM pg_database;'" % (username, hostname)

for database in os.popen(database_list_command).readlines():
    database = database.strip()
    if len(database) == 0 or database.startswith('-') or database.startswith('(') or database == 'datname' or database == 'template0':
        continue
    filename = "/mnt/Backup/dumps/pgsql/%s-%s.sql" % (database, filestamp)
    os.popen("pg_dump --create -U %s -h %s %s | gzip -c > %s.gz" % (username, hostname, database, filename))
