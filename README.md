# Quick test of reading and writing Pandas dataframes to MySQL.

## Quick-start

Deploy mysql in a container using the official mysql Docker image
<https://hub.docker.com/_/mysql> 

```bash
docker run --rm -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=passwd -d mysql
```

Install dedpendencies, and run test script which writes to and reads back a pandas dataframe from the database.

```bash
pipenv install
pipenv run python pandas_mysql_test.py
```

This test script can also be from inside a container, which avoids the need to install Python dependencies locally, using:

```bash
docker run -t --rm --network=container:mysql bmort/pandas-mysql-test
```

If sucessful the output of running the test should look something like:

<img src="https://raw.githubusercontent.com/bmort/pandas_sql_test/master/Screenshot%202019-08-02%20at%2002.16.15.png" width="609" height="334">

Once finished, clean up the mysql container with:

```bash
docker stop mysql
```
