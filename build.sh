#!/bin/bash

# Get the directory of the script file
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DATABASE_NAME="db_x23"
DATABASE_USER="db_user"
DATABASE_PASS="db_pass"

echo "
Cleaning up remnants of previous builds...
"
rm -rf venv build dist *.egg-info

echo "
Installing package dependencies...
"
sudo apt install -y postgresql postgresql-server-dev-all \
                    python3-pip python3-virtualenv

echo "
Creating the virtual environment...
"
virtualenv -p python3 venv
echo "
export DATABASE_NAME=${DATABASE_NAME}
export DATABASE_USER=${DATABASE_USER}
export DATABASE_PASS=${DATABASE_PASS}
" >> venv/bin/activate

echo "
Activating the virtual environment...
"
source venv/bin/activate

echo "
Installing Python dependencies...
"
pip install -r requirements.txt

echo "
Setting up Postgres database and run migrations...
"
echo "
create database ${DATABASE_NAME};
create user ${DATABASE_USER} with password '${DATABASE_PASS}';
alter role ${DATABASE_USER} set client_encoding to 'utf8';
alter role ${DATABASE_USER} set default_transaction_isolation to 'read committed';
alter role ${DATABASE_USER} set timezone to 'UTC';
grant all privileges on database ${DATABASE_NAME} TO ${DATABASE_USER};
" | sudo su - postgres -c psql
python manage.py makemigrations
python manage.py migrate

echo "
Creating admin superuser account for testing...
"
echo "from django.contrib.auth.models import User;
User.objects.filter(email='admin@example.com').delete();
User.objects.create_superuser('admin', 'admin@example.com', 'p@ssw0rd')
" | python manage.py shell
