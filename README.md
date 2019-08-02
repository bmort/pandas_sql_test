# Quick test of Pandas with Mysql

## Quick start

Deploy mysql in a container using the official mysql docker image
<https://hub.docker.com/_/mysql> and run python test script using this
database.

```bash
docker run --rm -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=passwd -d mysql
pipenv install
pipenv run python pandas_mysql_test.py
```

Run the `pandas_mysql_test.py` script also in a container
(`bmort/pandas-mysql-test`). This does not need the python dependencies to be
installed as they are provided in the container.:

```bash
docker run --rm -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=passwd -d mysql
docker run -t --rm --network=container:mysql bmort/pandas-mysql-test
```

Clean up the mysql container with:

```bash
docker stop mysql
```
