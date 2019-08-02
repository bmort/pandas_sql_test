FROM python:3.7-slim-buster

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
COPY pandas_mysql_test.py .

RUN pipenv install

ENTRYPOINT [ "pipenv", "run" ]
CMD [ "python3", "pandas_mysql_test.py"]
