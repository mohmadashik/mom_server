#!/bin/bash

source ../venv/bin/activate
rm -rf migrations   

date=$(date +%Y-%m-%d_%H-%M-%S)

mysqldump -u amohmad -p'Welcome' master_of_money >> ~/mm/bkp/mm_sql_bkp_"$date".sql

mysql -u amohmad -p'welcome' -e 'DROP DATABASE IF EXISTS master_of_money'

mysql -u amohmad -p'welcome' -e 'CREATE DATABASE master_of_money'

mysql -u amohmad -p'welcome' -D master_of_money -e 'DROP TABLE alembic_version'

export FLASK_APP=app/
flask db init
flask db migrate
flask db upgrade