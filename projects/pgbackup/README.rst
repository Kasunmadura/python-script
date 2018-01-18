pbbackup
=======

CLI for backing up remove Postgres database locally or to AWS s3.


Preparing for the Deverlopment
---------------------------------

1.Ensure 'pip' and 'pipenv' are installed
2.Clone this repo
3.Fetch devlopment dependencies: 'make install'


Usage
-----

Pass in a full database URl , the storage driver , and the destination.

S3 Example w/ bucket name:

::

  $ pgbackup postgres://demo@example.com:5432/db_name --driver s3 backup


Local Example with local path:

::

  $ pgbackup postgres://demo@example.com:5432/db_name --driver local /var/db_backup/dump.sql


Running test
------------

Run tests local using 'make' if virtualenv is active:

::

  $ make

if virtualenv env not actived

::

  $ pipenv run make
