FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install mysql-connector-python

CMD ["python", "mysql_task.py"]
