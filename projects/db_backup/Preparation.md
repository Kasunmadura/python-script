#Postgres db backup script


#### setup test bed

To setup the local test environment you can use /helper/db_setup.sh.it will help you to install postgres docker

verfiy postgres installtion:
      psql postgres://demo:password@serverip:80/sample -c "select * FROM employees;"


#### setup python test environment (virtualenv)

      pip install --user pipenv (sudo -H pip install -U pipenv)
      cd projects/db_backup
      (install python to supported pip environment)
      pip env install --two
